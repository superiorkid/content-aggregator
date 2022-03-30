from flask import Blueprint

scraping = Blueprint('scraping', __name__)

from . import routes
