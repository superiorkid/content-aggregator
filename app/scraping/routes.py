from . import scraping
from flask import render_template, request
from .scrapes import WebScrape
from app.feeds import BlogFeeds

@scraping.get('/geeksforgeeks')
def geeksforgeeks():
  blog = BlogFeeds()

  link = request.args.get('links')

  scrape = WebScrape()
  articles = scrape.geeks(link)

  programming_articles = blog.programming_section()
  opensource_articles = blog.opensource_section()

  return render_template('article/geeks.html', data=articles, title="Geeksforgeeks", programming=programming_articles, opensource=opensource_articles)

@scraping.get('/github_blog')
def github():
  blog = BlogFeeds()
  link = request.args.get('links')

  scrape = WebScrape()
  articles = scrape.github_blog(link)

  programming_articles = blog.programming_section()
  opensource_articles = blog.opensource_section()

  return render_template('article/github.html', data=articles, title="Github",programming=programming_articles, opensource=opensource_articles)

@scraping.get('/codingdojo')
def codingdojo():
  blog = BlogFeeds()
  link = request.args.get('links')

  scrape = WebScrape()
  articles = scrape.codingdojo(link)

  programming_articles = blog.programming_section()
  opensource_articles = blog.opensource_section()

  return render_template('article/codingdojo.html', data=articles, title="CodingDojo", programming=programming_articles, opensource=opensource_articles)

@scraping.get('/fosslinux')
def fosslinux():
  blog = BlogFeeds()
  link = request.args.get('links')

  scrape = WebScrape()
  articles = scrape.fosslinux(link)

  programming_articles = blog.programming_section()
  opensource_articles = blog.opensource_section()

  return render_template('article/fosslinux.html', data=articles, title="FossLinux",programming=programming_articles, opensource=opensource_articles)

@scraping.get('/linuxhint')
def linuxhint():
  blog = BlogFeeds()
  link = request.args.get('links')

  scrape = WebScrape()
  articles = scrape.linuxhint(link)

  programming_articles = blog.programming_section()
  opensource_articles = blog.opensource_section()

  return render_template('article/linuxhint.html', data=articles, title="Linux Hint", programming=programming_articles, opensource=opensource_articles)

@scraping.get('/itsfoss')
def itsfoss():
  blog = BlogFeeds()
  link = request.args.get('links')

  scrape = WebScrape()
  articles = scrape.itsfoss(link)

  programming_articles = blog.programming_section()
  opensource_articles = blog.opensource_section()


  return render_template('article/itsfoss.html', data=articles, title="It\'s Foss", programming=programming_articles, opensource=opensource_articles)


# @scraping.get('/ostechnix')
# def ostechnix():
#   link = request.args.get('links')

#   scrape = WebScrape()
#   articles = scrape.ostechnix(link)

#   return render_template('article/ostechnix.html', data=articles, title="OSTechNix")
