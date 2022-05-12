from . import feed

from flask import render_template
from app.feeds import BlogFeeds
from ..models import User
from flask_login import current_user

@feed.get('/explore')
def front_view():
  """
    front view berisikan gabungan dari semua feed
  """

  blog = BlogFeeds()

  data = blog.recent_update()
  programming_articles = blog.programming_section()
  opensource_articles = blog.opensource_section()

  if current_user.is_authenticated:
    bookmarks = current_user.bookmarks.all()
    return render_template('index.html', data = data, programming=programming_articles, opensource=opensource_articles, title = 'Explore', bookmarks=bookmarks)

  return render_template('index.html', data = data, programming=programming_articles, opensource=opensource_articles, title = 'Explore')


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
  blog = BlogFeeds()
  url = blog.programming.get('geeksforgeeks')

  articles = blog.individual_blog(url)
  programming_articles = blog.programming_section()
  opensource_articles = blog.opensource_section()

  return render_template('per_sites.html', title="OpenSource", data=articles, programming=programming_articles, opensource=opensource_articles)


@feed.get('/programming/codingdojo')
def codingdojo():
  """
    geek for geeks section
  """
  blog = BlogFeeds()
  url = blog.programming.get('codingdojo')

  articles = blog.individual_blog(url)
  programming_articles = blog.programming_section()
  opensource_articles = blog.opensource_section()

  if current_user.is_authenticated:
    bookmarks = current_user.bookmarks.all()
    return render_template('per_sites.html', title="CodingDojo latest", data=articles, programming=programming_articles, opensource=opensource_articles, bookmarks=bookmarks)

  return render_template('per_sites.html', title="CodingDojo latest", data=articles, programming=programming_articles, opensource=opensource_articles)


@feed.get('/programming/github')
def github():
  """
    geek for geeks section
  """
  blog = BlogFeeds()
  url = blog.programming.get('github')

  articles = blog.individual_blog(url)
  programming_articles = blog.programming_section()
  opensource_articles = blog.opensource_section()

  if current_user.is_authenticated:
    bookmarks = current_user.bookmarks.all()
    return render_template('per_sites.html', title="Github Blog latest", data=articles, programming=programming_articles, opensource=opensource_articles, bookmarks=bookmarks)

  return render_template('per_sites.html', title="Github Blog latest", data=articles, programming=programming_articles, opensource=opensource_articles)


@feed.get('/programming/linuxhint')
def linuxhint():
  """
    geek for geeks section
  """
  blog = BlogFeeds()
  url = blog.opensource.get('linuxhint')

  articles = blog.individual_blog(url)
  programming_articles = blog.programming_section()
  opensource_articles = blog.opensource_section()  

  return render_template('per_sites.html', title="LinuxHint latest", data=articles, programming=programming_articles, opensource=opensource_articles)


@feed.get('/programming/fosslinux')
def fosslinux():
  """
    geek for geeks section
  """
  blog = BlogFeeds()
  url = blog.opensource.get('fosslinux')

  articles = blog.individual_blog(url)
  programming_articles = blog.programming_section()
  opensource_articles = blog.opensource_section()

  if current_user.is_authenticated:
    bookmarks = current_user.bookmarks.all()
    return render_template('per_sites.html', title="Fosslinux latest", data=articles, programming=programming_articles, opensource=opensource_articles, bookmarks=bookmarks)

  return render_template('per_sites.html', title="Fosslinux latest", data=articles, programming=programming_articles, opensource=opensource_articles)



@feed.get('/programming/itsfoss')
def itsfoss():
  """
    geek for geeks section
  """
  blog = BlogFeeds()
  url = blog.opensource.get('itsfoss')

  articles = blog.individual_blog(url)
  programming_articles = blog.programming_section()
  opensource_articles = blog.opensource_section()

  if current_user.is_authenticated:
    bookmarks = current_user.bookmarks.all()
    return render_template('per_sites.html', title="It`s Foss latest", data=articles, programming=programming_articles, opensource=opensource_articles, bookmarks=bookmarks)

  return render_template('per_sites.html', title="It`s Foss latest", data=articles, programming=programming_articles, opensource=opensource_articles)

