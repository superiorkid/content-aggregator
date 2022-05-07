from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from . import login_manager
from flask import current_app
from itsdangerous.serializer import Serializer
from itsdangerous import BadSignature, SignatureExpired
from datetime import datetime, timedelta
from dateutil import tz
from hashlib import md5




class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, nullable=False)
  email = db.Column(db.String(80), index=True, nullable=False)
  password_hash = db.Column(db.String(128))
  confirmed = db.Column(db.Boolean, default=False)
  last_seen = db.Column(db.DateTime, default=datetime.utcnow)
  join_date = db.Column(db.DateTime, default=datetime.utcnow)
  role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
  bookmarks = db.relationship('Bookmark', backref='user', lazy='dynamic')

  def __init__(self, **kwargs):
    super(User, self).__init__(**kwargs)

    if self.role is None:
      if self.email == current_app.config['IS_ADMIN']:
        self.role = Role.query.filter_by(permissions=0xff).first()
      if self.role is None:
        self.role = Role.query.filter_by(default=True).first()

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

  def generate_email_changes_token(self, new_email):
    s = Serializer(current_app.config['SECRET_KEY'])
    return s.dumps({
        'reset': self.id,
        'new_email': new_email
      })

  def can(self, permissions):
    return self.role is not None  and (self.role.permissions & permissions) == permissions

  def is_administrator(self):
    return self.can(Permission.ADMINISTER)

  def avatar(self, size):
    digest = md5(self.email.lower().encode('utf-8')).hexdigest()
    return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

@staticmethod
def newest():
  recent = datetime.now(tz=tz.tzlocal()) - timedelta(hours=720) # 720 = 1 month
  return User.query.filter(User.join_date >= recent).order_by(User.join_date.desc()).all()

class AnonymousUser(AnonymousUserMixin):
  def can(self, permissions):
    return False

  def is_administrator(self):
    return False

login_manager.anonymous_user = AnonymousUser

class Permission:
  BOOKMARK = 0x01
  ADMINISTER = 0x02

class Role(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), unique=True)
  default = db.Column(db.Boolean, default=False, index=True)
  permissions = db.Column(db.Integer)
  users = db.relationship('User', backref='role', lazy='dynamic')

  def __repr__(self):
    return f'<Role {self.name}>'

  @staticmethod
  def insert_roles():
    roles = {
      'User': (Permission.BOOKMARK, True),
      'Administrator': (0xff, False)
    }

    for r in roles:
      role = Role.query.filter_by(name=r).first()
      if role is None:
        role = Role(name=r)

      role.permissions = roles[r][0]
      role.default = roles[r][1]
      db.session.add(role)
    db.session.commit()


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


class Bookmark(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  blog_name = db.Column(db.String)
  blog_img_url = db.Column(db.String)
  title =  db.Column(db.String(255), index=True)
  link = db.Column(db.String(255))
  posted = db.Column(db.DateTime)
  timestamp = db.Column(db.DateTime, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __repr__(self):
    return f'<Title {self.title}>'

