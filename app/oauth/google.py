from flask_login import current_user, login_user
from flask_dance.contrib.google import make_google_blueprint
from flask_dance.consumer import oauth_authorized, oauth_error
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from sqlalchemy.orm.exc import NoResultFound
from flask import flash, url_for, redirect
from .. import db
from ..models import User, OAuth


blueprint = make_google_blueprint(
	scope = ['profile', 'email'],
	storage=SQLAlchemyStorage(OAuth, db.session, user=current_user)
)

@oauth_authorized.connect_via(blueprint)
def google_logged_in(blueprint, token):
	if not token:
		flash('Failed to log in.', 'warning')
		return False

	resp = blueprint.session.get('/oauth2/v2/userinfo')
	if not resp.ok:
		flash('Failed to fetch user info', 'waring')
		return False

	google_info = resp.json()
	google_user_id = google_info['id']

	# find this oauth token in the database, or create it
	query = OAuth.query.filter_by(provider=blueprint.name, provider_user_id=google_user_id)
	try:
		oauth = query.one()
	except NoResultFound:
		google_user_login = str(google_info['email'])
		oauth = OAuth(provider=blueprint.name, provider_user_id=google_user_id, provider_user_login=google_user_login, token=token)

	# Now, figure out what to do with this token. There are 2x2 options:
    # user login state and token link state.
	if current_user.is_anonymous:
		if oauth.user:
			# If the user is not logged in and the token is linked,
			# log the user into the linked user account
			login_user(oauth.user)
			flash('Successfully signed in with Google', 'success')
		else:
			# If the user is not logged in and the token is unlinked,
			# create a new local user account and log that account in.
			# This means that one person can make multiple accounts, but it's
			# OK because they can merge those accounts later.
			user = User(username=google_info["name"], email=google_info['email'])
			user.confirmed = True
			oauth.user = user
			db.session.add_all([user, oauth])
			db.session.commit()
			login_user(user)
			flash("Successfully signed in with Google.", 'success')
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
			flash('Successfully linked Google account.', 'success')

    # Indicate that the backend shouldn't manage creating the OAuth object
    # in the database, since we've already done so!
	return False


# notify on OAuth provider error
@oauth_error.connect_via(blueprint)
def google_error(blueprint, message, response):
	msg = ("OAuth error from {name}! " "message={message} response={response}").format(name=blueprint.name, message=message, response=response)
	flash(msg, "warning")