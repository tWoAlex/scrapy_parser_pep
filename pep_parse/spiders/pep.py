import re

import scrapy

from pep_parse.items import PepParseItem


PEP_TITLE_REGEX = re.compile(r'PEP (?P<number>\d+) – (?P<title>.+)')


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        for link in response.css(
            'section[id=numerical-index] tbody a::attr(href)'
        ).getall():
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get()
        number, name = re.search(PEP_TITLE_REGEX, title).groups()
        status = response.css('dl.field-list abbr::text').get()
        yield PepParseItem(number=number,
                           name=name,
                           status=status)
