from app.feeds import BlogFeeds
from . import main
from flask import redirect, url_for
from ..decorators import admin_required
from flask_login import login_required


@main.get('/')
def index():
  return redirect(url_for('feed.front_view'))

@main.route('/admin')
@admin_required
@login_required
def admin():
  return 'hello ini admin page'
