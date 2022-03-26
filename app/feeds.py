import feedparser
import io
import re

from datetime import datetime
from dateutil import tz

class BlogFeeds(object):

  def __init__(self):
    self.__programming = {
      "https://www.geeksforgeeks.org/feed/",
      "http://feeds.feedburner.com/CssTricks",
      # "https://sdtimes.com/feed/",
      "https://scand.com/company/blog/feed/"
    }
    self.__opensource = {
      "https://www.cyberciti.biz/feed/",
      "https://itsfoss.com/feed/",
      "https://linuxhint.com/feed/",
      "https://ostechnix.com/feed/",
      "https://www.fosslinux.com/feed"
    }
    self.pattern = re.compile('<.*?>')

  @property
  def programming(self):
    return self.__programming

  @property
  def opensource(self):
    return self.__opensource

  def cleanhtml(self, raw_html: str):
    cleantext = re.sub(self.pattern, '', raw_html)
    return cleantext

  def parse_datetime(self, str_date: str):
    utc = datetime.strptime(str_date, '%a, %d %b %Y %H:%M:%S +0000')

    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Asia/Makassar')

    utc = utc.replace(tzinfo=from_zone)
    central = utc.astimezone(to_zone)

    return central

  def all_feeds(self):
    blog_url = self.opensource | self.programming

    blog_img = ''
    blog = [feedparser.parse(url) for url in blog_url]

    for i in blog:
      if 'image' in i.feed:
        blog_img = i.feed.image.href
      else:
        blog_img = None

    articles = [{'blog_title': feeds.feed.title, 'blog_img': blog_img, 'title': i.title, 'summary': self.cleanhtml(i.summary),'date': self.parse_datetime(i.published), 'link': i.link} for feeds in blog for i in feeds.entries]
    articles_sorted = sorted(articles, key=lambda x: x['date'], reverse=True)[:10]

    return articles_sorted


  def programming_section(self):
    url = self.programming

    blog_img = ''
    blog = [feedparser.parse(url) for url in url]

    for i in blog:
      if 'image' in i.feed:
        blog_img = i.feed.image.href
      else:
        blog_img = None

    articles = [{'blog_title': feeds.feed.title, 'blog_img': blog_img, 'title': i.title, 'summary': self.cleanhtml(i.summary),'date': self.parse_datetime(i.published), 'link': i.link} for feeds in blog for i in feeds.entries]
    articles_sorted = sorted(articles, key=lambda x: x['date'], reverse=True)

    return articles_sorted


  def opensource_section(self):
    url = self.opensource

    blog_img = ''
    blog = [feedparser.parse(url) for url in url]

    for i in blog:
      if 'image' in i.feed:
        blog_img = i.feed.image.href
      else:
        blog_img = None

    articles = [{'blog_title': feeds.feed.title, 'blog_img': blog_img, 'title': i.title, 'summary': self.cleanhtml(i.summary),'date': self.parse_datetime(i.published), 'link': i.link} for feeds in blog for i in feeds.entries]
    articles_sorted = sorted(articles, key=lambda x: x['date'], reverse=True)

    return articles_sorted
