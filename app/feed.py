import feedparser
import dateutil.parser

class BlogFeed:

  def __init__(self):
    self.__programming = {
      "https://www.geeksforgeeks.org/feed/",
      "http://feeds.feedburner.com/CssTricks",
      "http://feeds.dzone.com/home",
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

  def all_feed(self):
    url_merge = self.__opensource | self.__programming

    blog = [feedparser.parse(url) for url in url_merge]
    temp = []

    for i in blog:
      if 'image' in i.feed:
        temp.append({'blog_title': i.feed.title, 'blog_img': i.feed.image.href})
      else:
        temp.append({'blog_title': i.feed.title, 'blog_img': None})

    feeds = [feed.entries for feed in blog]
    feed = [item for feed in feeds for item in feed]
    feed.sort(key=lambda x: dateutil.parser.parse(x.['published']), reverse=True)

    res = [{'title': i['title'], 'date': i['published'], 'link': i['link']} for i in feed[:6]]

    return


feed1 = BlogFeed()
print(feed1.all_feed())

