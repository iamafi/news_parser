import requests
from bs4 import BeautifulSoup


def daryo_scraper(url):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, 'html.parser')
    body = soup.find("div", {"class": "postContent"}).text.replace('\n', '')
    return body


def kun_scraper(url):
    response = requests.get(url=url)
    # print(response)
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup)
    body = soup.find("div", {"class": "single-content"})
    paragraphs = body.find_all('p')
    ll = ''
    for p in paragraphs:
        ll += p.text + ' '
    return ll


def gazeta_scraper(url):
    response = requests.get(url=url)
    print(response)
    # soup = BeautifulSoup(response.content, 'html.parser')
    # body = soup.find("div", {"class": "article-text"})
    # print(soup)
    # paragraphs = body.find_all('p')
    # print(paragraphs)
    # return paragraphs
