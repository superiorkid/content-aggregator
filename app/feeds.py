import feedparser
import re

from datetime import datetime
from dateutil import tz

class BlogFeeds(object):

  def __init__(self):
    self.__programming = {
      "codingdojo": "https://www.codingdojo.com/blog/feed",
      # "github": "https://github.blog/feed/"
    }
    self.__opensource = {
      "fosslinux": "https://www.fosslinux.com/feed",
      "itsfoss": "https://itsfoss.com/feed/"
    }

    # self.pattern = re.compile('<.*?>')

  @property
  def programming(self):
    return self.__programming

  @property
  def opensource(self):
    return self.__opensource

  def cleanhtml(self, raw_html: str):
    """
    Given a string of raw text, remove all html tags
    
    :param raw_html: The raw text to be cleaned
    :type raw_html: str
    :return: The cleaned text.
    """
    cleantext = re.sub("[^-9A-Za-z ]", '', raw_html)
    return cleantext

  def parse_datetime(self, str_date: str):
    """
    Parse a string to datetime object
    
    :param str_date: The date string to be parsed
    :type str_date: str
    :return: A list of dictionaries.
    """
    utc = datetime.strptime(str_date, '%a, %d %b %Y %H:%M:%S +0000')
    return utc

  def recent_update(self):
    blog_url = self.opensource | self.programming

    blog = [feedparser.parse(url) for site, url in blog_url.items()]

    articles = [{'blog_title': feeds.feed.title, 'blog_img': feeds.feed.image.href, 'title': self.cleanhtml(i.title), 'summary': self.cleanhtml(i.summary),'date': self.parse_datetime(i.published), 'link': i.link} for feeds in blog for i in feeds.entries]
    articles_sorted = sorted(articles, key=lambda x: x['date'], reverse=True)

    return articles_sorted[:10]


  def programming_section(self):
    blog_url = self.programming

    blog = [feedparser.parse(url) for site, url in blog_url.items()]

    articles = [{'blog_title': feeds.feed.title, 'blog_img': feeds.feed.image.href, 'title': self.cleanhtml(i.title), 'summary': self.cleanhtml(i.summary),'date': self.parse_datetime(i.published), 'link': i.link} for feeds in blog for i in feeds.entries]
    articles_sorted = sorted(articles, key=lambda x: x['date'], reverse=True)

    return articles_sorted


  def opensource_section(self):
    blog_url = self.opensource

    blog = [feedparser.parse(url) for site, url in blog_url.items()]

    articles = [{'blog_title': feeds.feed.title, 'blog_img': feeds.feed.image.href, 'title': self.cleanhtml(i.title), 'summary': self.cleanhtml(i.summary),'date': self.parse_datetime(i.published), 'link': i.link} for feeds in blog for i in feeds.entries]
    articles_sorted = sorted(articles, key=lambda x: x['date'], reverse=True)

    return articles_sorted


  def individual_blog(self, url):
    blog_feed = feedparser.parse(url)
    # getting lists of blog entries via .entries
    posts = blog_feed.entries

    # dictionary for holding posts details
    posts_details = {"blog_title" : blog_feed.feed.title,
                    "blog_img" : blog_feed.feed.image.href}

    post_list = []

    # iterating over individual posts
    for post in posts:
        temp = dict()

        # if any post doesn't have information then throw error.
        try:
            temp["title"] = self.cleanhtml(post.title)
            temp["summary"] = self.cleanhtml(post.summary)
            temp['date'] = self.parse_datetime(post.published)
            temp['link'] = post.link
        except:
            pass

        post_list.append(temp)

    # storing lists of posts in the dictionary
    posts_details["posts"] = post_list

    return posts_details # returning the details which is dictionary

# blog = BlogFeeds()
# print(blog.individual_blog('https://www.geeksforgeeks.org/feed/'))
