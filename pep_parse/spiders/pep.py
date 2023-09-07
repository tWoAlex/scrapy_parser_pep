import re

import scrapy

from pep_parse.items import PepParseItem


PEP_TITLE_REGEX = re.compile(r'PEP (?P<number>\d+) – (?P<title>.+)')


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_links = (
            response
            .xpath('//section[@id="numerical-index"]')
            .xpath('//tbody')
            .css('a::attr(href)')
        ).getall()

        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get()
        number, name = re.search(PEP_TITLE_REGEX, title).groups()

        table = response.xpath('//dl[@class="rfc2822 field-list simple"]')
        lines = zip(table.css('dt::text').getall(),
                    table.css('dd *::text').getall(),)

        status = None
        for dt_text, dd_text in lines:
            if dt_text == 'Status':
                status = dd_text

        yield PepParseItem({'number': number,
                            'name': name,
                            'status': status})
