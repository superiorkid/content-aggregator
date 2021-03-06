import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
  SECRET_KEY = os.getenv('SECRET_KEY') or os.urandom(12)

  # database
  # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI') or "postgresql://superiorkid:root@localhost/aggregator"
  SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', '').replace('postgres://', 'postgresql://') or "postgresql://superiorkid:root@localhost/aggregator"
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  # email
  MAIL_SERVER ='smtp.gmail.com'
  MAIL_PORT = 465
  MAIL_USERNAME = os.getenv('MAIL_USERNAME')
  MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
  MAIL_USE_TLS = False
  MAIL_USE_SSL = True

  IS_ADMIN = os.getenv("IS_ADMIN")
  ONESPACEPIRATE_MAIL_SUBJECT_PREFIX = '[DemoGregator]'
  ONESPACEPIRATE_MAIL_SENDER = 'FakeGregator Admin <noreply@demogregator.com>'

  GITHUB_OAUTH_CLIENT_ID = os.getenv("GITHUB_OAUTH_CLIENT_ID")
  GITHUB_OAUTH_CLIENT_SECRET = os.getenv("GITHUB_OAUTH_CLIENT_SECRET")
  GOOGLE_OAUTH_CLIENT_ID = os.getenv("GOOGLE_OAUTH_CLIENT_ID")
  GOOGLE_OAUTH_CLIENT_SECRET = os.getenv("GOOGLE_OAUTH_CLIENT_SECRET")
  OAUTHLIB_RELAX_TOKEN_SCOPE = os.getenv('OAUTHLIB_RELAX_TOKEN_SCOPE')
  OAUTHLIB_INSECURE_TRANSPORT = os.getenv('OAUTHLIB_INSECURE_TRANSPORT')
