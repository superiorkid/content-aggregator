from . import scraping
from flask import render_template, request
from .scrapes import WebScrape

@scraping.get('/geeksforgeeks')
def geeksforgeeks():

  link = request.args.get('links')

  scrape = WebScrape()
  articles = scrape.geeks(link)

  return render_template('article/geeks.html', data=articles, title="GeeksForGeeks")

@scraping.get('/github_blog')
def github():
  link = request.args.get('links')

  scrape = WebScrape()
  articles = scrape.github_blog(link)

  return render_template('article/github.html', data=articles, title="Github")

@scraping.get('/codingdojo')
def codingdojo():
  link = request.args.get('links')

  scrape = WebScrape()
  articles = scrape.codingdojo(link)

  return render_template('article/codingdojo.html', data=articles)

@scraping.get('/ostechnix')
def ostechnix():
  pass

@scraping.get('/linuxtoday')
def linuxtoday():
  pass

@scraping.get('/itsfoss')
def itsfoss():
  link = request.args.get('links')

  scrape = WebScrape()
  articles = scrape.itsfoss(link)

  return render_template('article/itsfoss.html', data=articles)
