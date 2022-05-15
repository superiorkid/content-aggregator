from flask import flash, url_for, redirect
from flask_login import current_user, login_user
from flask_dance.contrib.github import make_github_blueprint
from flask_dance.consumer import oauth_authorized, oauth_error
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from sqlalchemy.orm.exc import NoResultFound
from ..models import User, OAuth
from .. import db


blueprint = make_github_blueprint(storage=SQLAlchemyStorage(OAuth, db.session, user=current_user))

# create/login login user on successfull Oauth login
@oauth_authorized.connect_via(blueprint)
def github_logged_in(blueprint, token):
	if not token:
		flash('Failed to login with Github', 'warning')
		return

	resp = blueprint.session.get('/user')
	if not resp.ok:
		flash('Failed to fetch user info from Github', 'warnig')
		return

	github_info = resp.json()
	github_user_id = str(github_info['id'])

	# find this oauth token in database, or create it
	query = OAuth.query.filter_by(provider=blueprint.name, provider_user_id=github_user_id)

	try:
		oauth = query.one()
	except NoResultFound:
		github_user_login = str(github_info['login'])
		oauth = OAuth(provider=blueprint.name, provider_user_id=github_user_id, provider_user_login=github_user_login, token=token)

	# now, figure out what do with this token. there are 2x2 options
	# user login state and token link state

	if current_user.is_anonymous:
		if oauth.user:
			# if the user is logged in and the token  is linked, check if these
			# accounts are the same
			login_user(oauth.user)
			flash('Successfully signed in with Github', 'success')
		else:
			# If the user is not logged in and the token is unlinked,
			# create a new local user account and log that account in.
			# This means that one person can make multiple accounts, but it's
			# OK because they can merge those accounts later.
			user = User(username=github_info['login'], email=github_info['email'])
			oauth.user = user
			user.confirmed = True
			db.session.add_all([user, oauth])
			db.session.commit()
			login_user(user)
			flash('Successfully signed in with Github', 'success')
	else:
		if oauth.user:
			# If the user is logged in and the token is linked, check if these
			# accounts are the same!
			if current_user != oauth.user:
				# Account collision! Ask user if they want to merge accounts.
				url = url_for('auth.merge', username=oauth.user.username)
				return redirect(url)
		else:
			# If the user is logged in and the token is unlinked,
			# link the token to the current user
			oauth.user = current_user
			db.session.add(oauth)
			db.session.commit()
			flash('Successfully linked GitHub account.', 'success')

    # Indicate that the backend shouldn't manage creating the OAuth object
    # in the database, since we've already done so!
	return False


# notify on oauth provider error
@oauth_error.connect_via(blueprint)
def github_error(blueprint, message, response):
	msg = ("OAuth error from {name}! " "message={message} response={response}").format(name=blueprint.name, message=message, response=response)
	flash(msg, 'warning')

