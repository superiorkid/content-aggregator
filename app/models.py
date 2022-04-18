from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from flask import current_app
from itsdangerous.serializer import Serializer
from itsdangerous import BadSignature, SignatureExpired


class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, nullable=False)
  email = db.Column(db.String(80), index=True, nullable=False)
  password_hash = db.Column(db.String(128))
  confirmed = db.Column(db.Boolean, default=False)

  def __repr__(self):
    return '<User {}>'.format(self.username)

  @property
  def password(self):
    raise AttributeError('password is not a readable attribute')

  @password.setter
  def password(self, passwords):
    self.password_hash = generate_password_hash(passwords)

  def verify_password(self, passwords):
    return check_password_hash(self.password_hash, passwords)

  # account confirmation
  def generate_confirmation_token(self):
    s = Serializer(current_app.config['SECRET_KEY'])
    return s.dumps({'confirm': self.id})

  def confirm(self, token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
      data = s.loads(token)
    except(BadSignature, SignatureExpired):
      return False

    if data.get('confirm') != self.id:
      return False

    self.confirmed = True
    db.session.add(self)
    db.session.commit()
    return True

  # reset password function
  #
  def generate_reset_token(self):
    s = Serializer(current_app.config['SECRET_KEY'])
    return s.dumps({'reset': self.id})

  # def reset(self, token):
  #   s = Serializer(current_app.config['SECRET_KEY'])
  #   try:
  #     data = s.loads(token)
  #   except(BadSignature, SignatureExpired):
  #     return False

  #   if data.get('reset') != self.id:
  #     return False

  #   return True

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))
