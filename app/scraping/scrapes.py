import requests

from bs4 import BeautifulSoup


class WebScrape:

  def geeks(self, url):
    self.url = url

    res = requests.get(self.url)
    soup = BeautifulSoup(res.content, 'html.parser')
    articles = soup.article.find(class_="text")

    # articles = soup.article

    unwanted = articles.find(id="personalNoteDiv")
    unwanted.replaceWith()

    return articles


  def css_tricks(self, url):
    self.url = url

    res = requests.get(self.url)
    soup = BeautifulSoup(res.content, 'html.parser')
    articles = soup.article

    return articles




# geeksforgeeks = WebScrape()

# print(geeksforgeeks.geeks('https://www.geeksforgeeks.org/top-5-features-of-java-17-that-you-must-know/'))
