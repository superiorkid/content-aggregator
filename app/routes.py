from app import app
from flask import render_template

@app.get('/')
def index():
  """
    front view berisikan gabungan dari semua feed
  """

  return render_template('index.html', title='Front view')


@app.get('/programming')
def programming():
  """
    programming section
  """
  pass


@app.get('/opensource')
def open_source():
  """
    open source section
  """
  pass


@app.get('/programming/geekforgeeks')
def geek_for_geeks():
  """
    geek for geeks section
  """
  pass


# etc
