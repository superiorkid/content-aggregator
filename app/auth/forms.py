from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, DataRequired, Length


class LoginForm(FlaskForm):
  email = StringField('Email', validators=[Required(), Email(), Length(1, 64)])
  password = PasswordField('Password', validators=[Required()])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Sign In')
