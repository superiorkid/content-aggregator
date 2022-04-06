import requests
import re

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
      if len(x.get_text(strip=True)) == 0 and x.name not in ['div', 'img', 'br']:
          x.extract()

    unwanted = body.find(id='personalNoteDiv')
    unwanted.replaceWith('')

    # unwanted = body.find(id='GFG_AD_Desktop_InContent_ATF_728x280')
    # unwanted.replaceWith('')
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
    body = soup.find(class_='entry-content')

    temp = {
      "title": soup.find('h1', class_="entry-title").get_text(),
      "body": body
    }

    return temp

  def fosslinux(self, url):
    self.url = url

    res = requests.get(self.url)
    soup = BeautifulSoup(res.content, 'html.parser')

    body = soup.find('div', class_="tdb_single_content")

    temp = {
      "title": soup.find('h1', class_="tdb-title-text").get_text(),
      "body": body
    }

    unwanted = body.find('div', class_="id_ad_content-horiz-center")
    unwanted.replaceWith()

    unwanted = body.find('div', class_="id_bottom_ad")
    unwanted.replaceWith()

    for img in body.find_all('img'):
      img['src'] = img.get('data-src')

    return temp

  def linuxhint(self, url):
    self.url = url

    res = requests.get(self.url)
    soup = BeautifulSoup(res.content, 'html.parser')

    articles = soup.article
    body = articles.find('div', class_="entry-content")

    temp = {
      "title": articles.find('h1', class_="entry-title").get_text(),
      "body": body
    }

    for img in body.find_all('img'):
      img['src'] = img.get('data-lazy-src')

    return temp

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

# print(geeksforgeeks.ostechnix('https://ostechnix.com/create-linux-disk-partitions-with-fdisk/'))
