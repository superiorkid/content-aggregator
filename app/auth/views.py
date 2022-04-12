from flask import render_template, redirect, request, url_for, flash
from . import auth
from ..models import User
from .forms import LoginForm, RegistrationForm
from flask_login import login_user, logout_user, login_required
from .. import db

@auth.get('/login')
@auth.post('/login')
def login():
  form = LoginForm()

  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()

    if user is not None and user.verify_password(form.password.data):
      login_user(user, form.remember_me.data)
      return redirect(request.args.get('next') or url_for('main.index'))

    flash('Invalid email or password.')

  return render_template('auth/login.html', form=form, title='Sign In')


@auth.get('/register')
@auth.post('/register')
def register():
  form = RegistrationForm()

  if form.validate_on_submit():
    user = User(email=form.email.data, username=form.username.data, password=form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('You can now login')
    return redirect(url_for('auth.login'))

  return render_template('auth/register.html', form=form)


@auth.route('/logout')
@login_required
def logout():
  logout_user()
  flash('Successfully user logout')
  return redirect(url_for('main.index'))
