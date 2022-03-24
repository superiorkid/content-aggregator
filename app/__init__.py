from flask import Flask
from flask_bootstrap import Bootstrap5

bootstrap = Bootstrap5()

def create_app():
  app = Flask(__name__)

  bootstrap.init_app(app)

  # blueprint init
  from .feed import feed as feed_blueprint
  from .main import main as main_blueprint

  app.register_blueprint(feed_blueprint, url_prefix='/blog')
  app.register_blueprint(main_blueprint)

  return app
