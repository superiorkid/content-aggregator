import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(12)

  # database
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgresql://superiorkid:root@localhost/aggregator"
  SQLALCHEMY_TRACK_MODIFICATIONS = False
