import feedparser
import dateutil.parser

from prettyprinter import pprint


class BlogFeed:

  def __init__(self):
    self.__programming = {
      "https://www.geeksforgeeks.org/feed/",
      "http://feeds.feedburner.com/CssTricks",
      "https://sdtimes.com/feed/",
      "https://scand.com/company/blog/feed/"
    }

    self.__opensource = {
      "https://www.cyberciti.biz/feed/",
      "https://itsfoss.com/feed/",
      "https://linuxhint.com/feed/",
      "https://ostechnix.com/feed/",
      "https://www.fosslinux.com/feed"
    }

  @property
  def programming(self):
    return self.__programming

  @property
  def opensource(self):
    return self.__opensource

  def all_feeds(self):
    blog_url = self.__opensource | self.__programming

    blog_img = ''
    blog = [feedparser.parse(url) for url in blog_url]

    for i in blog:
      if 'image' in i.feed:
        blog_img = i.feed.image.href
      else:
        blog_img = None

    articles = [{'blog_title': feeds.feed.title, 'blog_img': blog_img, 'title': i.title, 'summary': i.summary, 'date': i.published, 'link': i.link} for feeds in blog for i in feeds.entries]
    articles_sorted = sorted(articles, key=lambda x: dateutil.parser.parse(x['date']), reverse=True)[:9]

    return articles_sorted

