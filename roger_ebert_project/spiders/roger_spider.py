import scrapy


class RogerSpiderSpider(scrapy.Spider):
    name = 'roger_spider'
    allowed_domains = ['www.rogerebert.com']
    start_urls = ['http://www.rogerebert.com/']

    def parse(self, response):
        pass
