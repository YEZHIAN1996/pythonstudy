import scrapy
from scrapy.http.request.form import FormRequest
from _cffi_backend import callback

class LoginSpider(scrapy.Spider):
    name = 'LoginSpider'
    # allowed_domains = ['LoginSpider.com']
    # start_urls = ['http://LoginSpider.com/']

    def start_requests(self):
        return [
            FormRequest('http://localhost:5000/static/login.html', callback=self.parseLogin)
        ]

    def parseLogin(self, response):
        return FormRequest.from_response(response, formdata={'username': 'bill', 'password': '1234'})

    def parse(self, response):
        text = response.xpath('//h1/text()').extract()
        print(text[0])



