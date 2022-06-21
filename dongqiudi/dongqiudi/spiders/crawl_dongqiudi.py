import scrapy


class CrawlDongqiudiSpider(scrapy.Spider):
    name = 'crawl_dongqiudi'
    allowed_domains = ['dongqiudi.com']
    start_urls = ['http://dongqiudi.com/']

    def parse(self, response):
        pass
