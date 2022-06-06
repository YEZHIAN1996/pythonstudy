import scrapy
from bs4 import *
from itemloaders import ItemLoader
from myscrapy.items import MyscrapyItem
from scrapy.loader.processors import *

class ItemLoaderSpider(scrapy.Spider):
    name = 'ItemLoaderSpider'
    start_urls = [
        'https://geekori.com/blogsCenter.php?uid=geekori'
    ]
    def parse(self, response):
        itemLoader = ItemLoader(item=MyscrapyItem(), response=response)
        itemLoader.add_xpath('title', '//*[@id="all"]/div[1]/section/div[2]/h2/a/text()')
        itemLoader.add_xpath('href', '//*[@id="all"]/div[1]/section/div[2]/h2/a/@href', MapCompose(lambda href: 'https://geekori.com/' + href))
        itemLoader.add_xpath('abstract', '//*[@id="all"]/div[1]/section/div[2]/p/text()')
        return itemLoader.load_item()