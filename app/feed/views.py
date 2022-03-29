from . import feed

from flask import render_template
from app.feeds import BlogFeeds


@feed.get('/all')
def front_view():
  """
    front view berisikan gabungan dari semua feed
  """

  blog = BlogFeeds()

  data = blog.recent_update()
  programming_articles = blog.programming_section()
  opensource_articles = blog.opensource_section()

  return render_template('index.html',data = data, programming=programming_articles, opensource=opensource_articles, title = 'Front view')



@feed.get('/programming')
def programming():
  """
    programming section
  """
  blog = BlogFeeds()
  programming_articles = blog.programming_section()

  return render_template('programming.html', title='Programming', data=programming_articles)


@feed.get('/opensource')
def opensource():
  """
    open source section
  """
  blog= BlogFeeds()
  opensource_articles = blog.opensource_section()

  return render_template('opensource.html', title="OpenSource", data=opensource_articles)


@feed.get('/programming/geekforgeeks')
def geek_for_geeks():
  """
    geek for geeks section
  """
  return 'ini /blog/programming/geekforgeeks'


# etc
