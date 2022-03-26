from . import feed

from flask import render_template
from app.feeds import BlogFeeds


@feed.get('/all')
def front_view():
  """
    front view berisikan gabungan dari semua feed
  """

  blog = BlogFeeds()

  data = blog.all_feeds()
  programming_articles = blog.programming_section()

  return render_template('index.html',data = data, programming=programming_articles, title = 'Front view')



@feed.get('/programming')
def programming():
  """
    programming section
  """
  blog = BlogFeeds()
  programming_articles = blog.programming_section()

  return render_template('programming.html', title='Programming', data=programming_articles)


@feed.get('/opensource')
def open_source():
  """
    open source section
  """
  return 'ini /blog/opensource'


@feed.get('/programming/geekforgeeks')
def geek_for_geeks():
  """
    geek for geeks section
  """
  return 'ini /blog/programming/geekforgeeks'


# etc
