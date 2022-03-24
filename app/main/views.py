from . import main
from flask import render_template


@main.get('/')
def index():
  """
    front view berisikan gabungan dari semua feed
  """

  return render_template('index.html', title='Front view')
