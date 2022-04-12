from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, nullable=False)
  email = db.Column(db.String(80), index=True, nullable=False)
  password_hash = db.Column(db.String(128))

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


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))
