from scrapy import cmdline

cmdline.execute('scrapy crawl SaveBlogSpider -o blog.xml'.split())