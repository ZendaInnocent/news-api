# Spider for dar24.com

import scrapy
from bs4 import BeautifulSoup


def get_link(item):
    return item.find('h2', {'class': 'title'}).find('a').get('href')


def get_title(item):
    return item.find('h2', {'class': 'title'}).find('a').text


def get_image_url(item):
    return item.find(
        'div', {'class': 'fl-picture'}).find('img').get('src')


class Dar24Spider(scrapy.Spider):
    name = 'dar24'

    start_urls = [
        'https://dar24.com/',
    ]

    def parse(self, response, **kwargs):
        # extracting data - link, image, title
        soup = BeautifulSoup(response.body, 'lxml')
        container = soup.find('div', {'id': 'fl-post-container'})
        articles = container.find_all('article')

        for article in articles:
            try:
                yield {
                    'image_url': get_image_url(article),
                    'title': get_title(article),
                    'link': get_link(article),
                    'source': 'dar24',
                }
            except AttributeError:
                pass
