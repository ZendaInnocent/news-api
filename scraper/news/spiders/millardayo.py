# Spider for MillardAyo.com

import scrapy
from bs4 import BeautifulSoup


class MillardAyoSpider(scrapy.Spider):
    name = 'millardayo'
    allowed_urls = ['www.millardayo.com']

    start_urls = [
        'https://millardayo.com',
    ]

    def parse(self, response, **kwargs):
        # extracting data - link, image, title, excerpt
        soup = BeautifulSoup(response.body, 'lxml')

        posts = soup.find_all('li', {'class': 'infinite-post'})

        for post in posts:
            try:
                yield {
                    'image_url': post.find('img').get('src'),
                    'link': post.find('a').get('href'),
                    'title': post.find('a').get('title'),
                    'excerpt': post.find('p').get_text(),
                    'source': 'millardayo',
                }
            except AttributeError:
                pass

        next_page = soup.find('a', text='Next ›').get('href')

        if next_page:
            yield response.follow(next_page, callback=self.parse)
