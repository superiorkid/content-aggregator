import feedparser
import dateutil.parser

urls = [
  "https://www.geeksforgeeks.org/feed/",
  "https://dev.to/feed",
  "https://joelhooks.com/rss.xml"
]

feeds = [feedparser.parse(url)['entries'] for url in urls]

feed = [item for feed in feeds for item in feed]
feed.sort(key=lambda x: dateutil.parser.parse(x['published']), reverse=True)

f = [{'title': i['title'], 'date': i['published'], 'link': i['link']} for i in feed[:10]]

print(f)


