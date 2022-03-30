from . import scraping
from flask import render_template, request
from .scrapes import WebScrape

@scraping.get('/geeksforgeeks')
def geeksforgeeks():

  link = request.args.get('links')

  scrape = WebScrape()
  articles = scrape.geeks(link)

  return render_template('geeks.html', data=articles)


