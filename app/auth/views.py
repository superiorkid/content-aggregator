from flask import render_template, redirect, request, url_for, flash, current_app
from . import auth
from ..models import User
from .forms import LoginForm, RegistrationForm, PasswordUpdatesForm, EmailForm, PasswordForm
from flask_login import login_user, logout_user, login_required, current_user
from .. import db
from ..email import send_mail
from itsdangerous.serializer import Serializer

@auth.get('/login')
@auth.post('/login')
def login():
  form = LoginForm()

  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()

    if user is not None and user.verify_password(form.password.data):
      login_user(user, form.remember_me.data)
      return redirect(request.args.get('next') or url_for('main.index'))

    flash('Invalid email or password.', 'warning')

  return render_template('auth/login.html', form=form, title='Sign In')


@auth.get('/register')
@auth.post('/register')
def register():
  form = RegistrationForm()

  if form.validate_on_submit():
    user = User(email=form.email.data, username=form.username.data, password=form.password.data)
    db.session.add(user)
    db.session.commit()

    # send token
    token = user.generate_confirmation_token()
    send_mail(user.email, 'Confirm Your Account', 'auth/email/confirm', user=user, token=token)

    flash('A confirmation email has been sent to you by email.', 'success')
    return redirect(url_for('main.index'))

  return render_template('auth/register.html', form=form)


@auth.route('/logout')
@login_required
def logout():
  logout_user()
  flash('Successfully user logout', 'success')
  return redirect(url_for('main.index'))


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
  if current_user.confirmed:
    return redirect(url_for('main.index'))

  if current_user.confirm(token):
    flash('You have confirmed account. Thanks.', 'success')
  else:
    flash('The confirmation link is invalid or has expired', 'danger')

  return redirect(url_for('main.index'))


@auth.before_app_request
def before_request():
  if current_user.is_authenticated and not current_user.confirmed and request.endpoint[:5] != 'auth.':
    return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
  if current_user.is_anonymous or current_user.confirmed:
    return redirect('main.index')

  return render_template('auth/unconfirmed.html')


@auth.route('/confirm')
@login_required
def resend_confirmation():
  token = current_user.generate_confirmation_token()
  send_mail(current_user.email, 'Confirm Your Account', 'auth/email/confirm', user=current_user.username, token=token)
  flash('A new confirmation email has been sent to you by email.', 'warning')
  return redirect(url_for('main.index'))


@auth.get('/password_update')
@auth.post('/password_update')
@login_required
def password_updates():
  form = PasswordUpdatesForm()

  if form.validate_on_submit(): #post method
    user = User.query.filter_by(username=current_user.username).first()

    if not user.verify_password(form.old_password.data):
      flash('rememeber your old password.')
      return redirect(url_for('auth.password_updates', 'warning'))

    if user is not None and user.verify_password(form.old_password.data):
      user.password = form.new_password.data
      db.session.commit()
      flash('Password update successfully', 'success')
      return redirect(url_for('main.index'))

  return render_template('auth/new_password.html', form=form, title='New Password')


@auth.get('/reset')
@auth.post('/reset')
def reset():
  form = EmailForm()

  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    try:
      token = user.generate_reset_token()
      send_mail(user.email, 'Reset Your Password', 'auth/email/reset', user=user.username, token=token)
      flash('A reset url has been sent to you by email', 'warning')
      return redirect(url_for('main.index'))
    except:
      flash('Your email has not registered', 'warning')
      return redirect(url_for('auth.reset'))

  return render_template('auth/reset.html', form=form)

@auth.get('/reset/<token>')
@auth.post('/reset/<token>')
def reset_token(token):
  form = PasswordForm()

  if form.validate_on_submit():
    s = Serializer(current_app.config['SECRET_KEY'])
    data = s.loads(token)
    user = User.query.filter_by(id=data.get('reset')).first()
    user.password = form.password.data
    db.session.commit()
    flash('Password Update successfully', 'success')
    return redirect(url_for('auth.login'))

  return render_template('auth/new_password.html', form=form)
