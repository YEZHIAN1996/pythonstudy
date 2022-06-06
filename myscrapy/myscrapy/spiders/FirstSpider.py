import scrapy
class Test1Spaider(scrapy.Spider):
    name = 'FirstSpider'
    start_urls = [
        'https://www.taobao.com'
    ]
    def parse(self, response):
        self.log('hello world')