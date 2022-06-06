import scrapy
from bs4 import *
from myscrapy.items import MyscrapyItem

class BlogSpider(scrapy.Spider):
    name = 'SaveBlogSpider'
    start_urls = [
        'https://geekori.com/blogsCenter.php?uid=geekori'
    ]
    def parse(self, response):
        item = MyscrapyItem()
        sectionList = response.xpath('//*[@id="all"]/div[1]/section').extract()
        for section in sectionList:
            bs = BeautifulSoup(section, 'lxml')
            artictDict = {}
            a = bs.find('a')
            artictDict['title'] = a.text
            artictDict['href'] = 'https://geekori.com/' + a.get('href')
            p = bs.find('p', class_ = 'excerpt')
            artictDict['abstract'] = p.text
            item['title'] = artictDict['title']
            item['href'] = artictDict['href']
            item['abstract'] = artictDict['abstract']

        return item
