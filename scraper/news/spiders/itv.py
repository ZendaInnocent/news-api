# Spider for itv.co.tz

import scrapy
from bs4 import BeautifulSoup


def get_link(item):
    return item.find('span', {'class': 'field-content'}).find('a').get('href')


def get_title(item):
    return item.find('span', {'class': 'field-content'}).find('a').text


def get_image_url(item):
    return item.find(
        'div', {'class': 'views-field-field-image'}).find('img').get('src')


def get_excerpt(item):
    return item.find('div', {'class': 'views-field-body'}).find('div').text


class ITVSpider(scrapy.Spider):
    name = 'itv'
    allowed_urls = ['www.itv.co.tz']

    start_urls = [
        'https://www.itv.co.tz/news',
    ]

    def parse(self, response, **kwargs):
        # extracting data - link, image, title, excerpt
        soup = BeautifulSoup(response.body, 'lxml')
        container = soup.find('div', {'class': 'region region-row1'})
        views_rows = container.find_all('div', {'views-row'})

        for views_row in views_rows:
            try:
                yield {
                    'image_url': get_image_url(views_row),
                    'title': get_title(views_row),
                    'link': f'https://www.itv.co.tz{get_link(views_row)}',
                    'excerpt': get_excerpt(views_row),
                }
            except AttributeError:
                pass

        next_page = soup.find('a', {'title': 'Go to next page'}).get('href')

        if next_page:
            yield response.follow(next_page, callback=self.parse)
