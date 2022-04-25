import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(12)

  # database
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or "postgresql://superiorkid:root@localhost/aggregator"
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  # email
  MAIL_SERVER = 'smtp.gmail.com'
  MAIL_PORT = 465
  MAIL_USE_TLS = False
  MAIL_USE_SSL = True
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  MAIL_SUPPRESS_SEND = False

  ONESPACEPIRATE_MAIL_SUBJECT_PREFIX = '[OneSpacePirate]'
  ONESPACEPIRATE_MAIL_SENDER = 'OneSpacePirate Admin <noreply@onespacepirate.com>'

