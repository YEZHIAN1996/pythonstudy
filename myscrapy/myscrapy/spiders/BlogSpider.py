import scrapy
from bs4 import *

class BlogSpider(scrapy.Spider):
    name = 'BlogSpider'
    start_urls = [
        'https://geekori.com/blogsCenter.php?uid=geekori'
    ]
    def parse(self, response):
        sectionList = response.xpath('//*[@id="all"]/div[1]/section').extract()
        for section in sectionList:
            bs = BeautifulSoup(section, 'lxml')
            artictDict = {}
            a = bs.find('a')
            artictDict['title'] = a.text
            artictDict['href'] = 'https://geekori.com/' + a.get('href')
            p = bs.find('p', class_ = 'excerpt')
            artictDict['abstract'] = p.text
            print(artictDict)