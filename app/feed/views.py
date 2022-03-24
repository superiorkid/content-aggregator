from . import feed
from flask import render_template


@feed.get('/programming')
def programming():
  """
    programming section
  """
  return 'ini /blog/programming'


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
