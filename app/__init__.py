from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

# import config
from config import Config

bootstrap = Bootstrap5()
moment = Moment()
db = SQLAlchemy()

def page_not_found(e):
  return render_template('error/404.html'), 404


def internal_server_error(e):
  return render_template('error/500.html'), 500


def create_app():
  """
  Create an app instance and register the blueprints
  :return: The app object.
  """
  app = Flask(__name__)
  app.config.from_object(Config)

  bootstrap.init_app(app)
  moment.init_app(app)
  db.init_app(app)

  # blueprint init
  from .feed import feed as feed_blueprint
  from .main import main as main_blueprint
  from .scraping import scraping as scrape_blueprint
  from .auth import auth as auth_blueprint

  app.register_blueprint(feed_blueprint, url_prefix='/feed')
  app.register_blueprint(main_blueprint)
  app.register_blueprint(scrape_blueprint, url_prefix='/feed/article')
  app.register_blueprint(auth_blueprint, url_prefix='/auth')

  # error handling
  app.register_error_handler(404, page_not_found)
  app.register_error_handler(500, internal_server_error)

  return app
