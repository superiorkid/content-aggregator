from . import admin
from ..decorators import admin_required
from flask_login import login_required
from flask import render_template
from ..models import User

@admin.route('/')
@admin_required
@login_required
def dashboard():
  users = User.query.all()
  articles_total = 0

  for user in users:
    articles_total += len(user.bookmarks.all())

  return render_template('admin/index.html', users=users, articles_total=articles_total)
