from app.feeds import BlogFeeds
from . import main
from flask import redirect, url_for


@main.get('/')
def index():
  # return redirect('/blog/all')
  return redirect(url_for('feed.front_view'))
