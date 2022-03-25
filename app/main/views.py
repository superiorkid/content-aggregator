from . import main
from flask import render_template
from ..feed import BlogFeed


@main.get('/')
def index():
  """
    front view berisikan gabungan dari semua feed
  """

  blog = BlogFeed()
  data = blog.all_feeds()

  return render_template('index.html',data = data, title = 'Front view')
