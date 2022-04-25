from flask import render_template, redirect, request, url_for, flash, current_app
from . import auth
from ..models import User
from .forms import LoginForm, RegistrationForm, PasswordUpdatesForm, EmailForm, PasswordForm
from flask_login import login_user, logout_user, login_required, current_user
from .. import db
from ..email import send_mail
from itsdangerous.serializer import Serializer
from itsdangerous import BadSignature, SignatureExpired

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
      flash('rememeber your old password.', 'warning')
      return redirect(url_for('auth.password_updates'))

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
    if user:
      token = user.generate_reset_token()
      send_mail(user.email, 'Reset Your Password', 'auth/email/reset', user=user.username, token=token)
      flash('A reset url has been sent to you by email', 'warning')
      return redirect(url_for('main.index'))

    flash('Your email has not registered', 'warning')

  return render_template('auth/reset.html', form=form)

@auth.get('/reset/<token>')
@auth.post('/reset/<token>')
def reset_token(token):
  form = PasswordForm()
  s = Serializer(current_app.config['SECRET_KEY'])

  if form.validate_on_submit():
    try:
      data = s.loads(token)
    except(BadSignature, SignatureExpired):
      flash('The confirmation link is invalid or has expired', 'danger')
      return redirect(url_for('auth.reset'))

    user = User.query.filter_by(id=data.get('reset')).first()
    user.password = form.password.data
    db.session.commit()
    flash('Password Update successfully', 'success')
    return redirect(url_for('auth.login'))

  return render_template('auth/reset_password.html', form=form)


@auth.get('/confirm_password')
@auth.post('/confirm_password')
@login_required
def password_cofirm_email_changes():
  form = PasswordForm()

  if form.validate_on_submit():
    user = User.query.filter_by(id=current_user.id).first()

    if user.verify_password(form.password.data):
      return redirect(url_for('auth.email_change'))

    flash('Your password wrong, try again', 'danger')

  return render_template('auth/reset_password.html', form=form)


@auth.get('/change_email')
@auth.post('/change_email')
@login_required
def email_change():
  form = EmailForm()

  if form.validate_on_submit():

    # email exist?
    if User.query.filter_by(email=form.email.data).first():
      flash('Email already  registered, try another email', 'warning')
      return redirect(request.url)

    user = User.query.filter_by(id=current_user.id).first()
    token = user.generate_email_changes_token(form.email.data)
    send_mail(form.email.data, 'Changes Your E-mail', 'auth/email/email_change', user=user, token=token)
    flash('A new confirmation email has been sent to you by email.', 'warning')

  return render_template('auth/change_email.html', form=form)

@auth.get('change_email/<token>')
@auth.post('change_email/<token>')
@login_required
def confirm_email_change(token):
  s = Serializer(current_app.config['SECRET_KEY'])

  try:
    data = s.loads(token)
  except(BadSignature, SignatureExpired):
    flash('The confirmation link is invalid or has expired', 'danger')
    return redirect(url_for('auth.email_change'))

  user = User.query.filter_by(id=current_user.id).first()
  user.email = data.get('new_email')
  db.session.add(user)
  db.session.commit()
  flash('Your email successfully changes', 'success')
  return redirect(url_for('main.index'))

