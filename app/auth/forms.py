from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import Email, DataRequired, Length, Regexp, EqualTo
from ..models import User


class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 64)])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
  username = StringField('Username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Usernames must have only letters, numbers, dots or underscores')])
  password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password', 'Password must match.')])
  confirm_password =PasswordField('Confirm Password', validators=[DataRequired()])
  submit = SubmitField('Register')

  def validate_email(self, email):
    if User.query.filter_by(email=email.data).first():
      raise ValidationError('Email already registered.')

  def validate_username(self, username):
    if User.query.filter_by(username=username.data).first():
      raise ValidationError('Username already in use.')

class PasswordUpdatesForm(FlaskForm):
  old_password = PasswordField('Old Password', validators=[DataRequired()])
  new_password = PasswordField('New Password', validators=[DataRequired(), EqualTo('confirm_new_password', 'Password must match.')])
  confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired()])
  submit = SubmitField('Update')


# form reset password
class PasswordForm(FlaskForm):
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Update')

class EmailForm(FlaskForm):
  email = StringField('Email Address', validators=[DataRequired(), Email()])
  submit = SubmitField('Send Link')


