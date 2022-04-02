import requests

from bs4 import BeautifulSoup
from markupsafe import Markup


class WebScrape:

  def geeks(self, url):
    self.url = url
    res = requests.get(self.url)
    soup = BeautifulSoup(res.content, 'html.parser')

    articles = soup.article
    body = articles.find('div', class_='text')


    temp = {
      'title': articles.find('h1').get_text(),
      'body': body
    }

    # remove empty tag
    for x in soup.find_all():
      if len(x.get_text(strip=True)) == 0 and x.name not in ['br', 'img']:
          x.extract()

    unwanted = body.find(id='personalNoteDiv')
    unwanted.replaceWith('')

    return temp


  def github_blog(self, url):
    self.url = url

    res = requests.get(self.url)
    soup = BeautifulSoup(res.content, 'html.parser')

    body = soup.find(class_="post__content")

    temp = {
      "title": soup.find(class_='post-hero').find('h1').get_text(),
      "body": body
    }

    unwanted = body.find('div', class_="f5-mktg")
    unwanted.replaceWith('')

    for i in body.find_all('img'):
      del i["srcset"]

    return temp

  def codingdojo(self, url):
    self.url = url

    res = requests.get(self.url)
    soup = BeautifulSoup(res.content, 'html.parser')
    articles = soup.find(class_='entry-content')

    return articles

  def ostechnix(self, url):
    pass


  def liunxtoday(self, url):
    pass


  def itsfoss(self, url):
    self.url = url

    res = requests.get(self.url)
    soup = BeautifulSoup(res.content, 'html.parser')
    body = soup.find(class_='entry-content')

    temp = {
      "title": soup.find(class_="entry-title").get_text(),
      "body": body
    }

    unwanted = body.find('div', class_="ss-inline-share-wrapper")
    unwanted.replaceWith()

    for img in body.find_all('img'):
      del img["srcset"]

    for iframe in body.find_all('iframe'):
      iframe['src'] = iframe.get('data-lazy-src')

    return temp



# geeksforgeeks = WebScrape()

# print(geeksforgeeks.itsfoss('https://itsfoss.com/accent-color-ubuntu/'))
