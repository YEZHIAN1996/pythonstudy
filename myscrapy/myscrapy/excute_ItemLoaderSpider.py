from scrapy import cmdline

cmdline.execute('scrapy crawl ItemLoaderSpider -o item1.json'.split())