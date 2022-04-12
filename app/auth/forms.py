from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Email, DataRequired, Length


class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 64)])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Sign In')
