# from lxml import *
from lxml import etree
import requests
import json

# 更具url抓取html代码，并返回这些代码，如果抓取失败，返回None
def getOnePage(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.text
        return None
    except Exception:
        return None

# 分析代码，这是一个产生器函数
def parseOnepage(html):
    selector = etree.HTML(html)
    # 选择tr节点
    items = selector.xpath('//tr[@class="item"]')
    # 在tr节点内部继续使用xpath选择对应的节点
    for item in items:
        book_infos = item.xpath('td/p/text()')[0]
        yield {
            # 图书名称
            'name': item.xpath('td/div/a/@title')[0],
            # 获取图书主页链接
            'url': item.xpath('td/div/a/@href')[0],
            # 作者
            'author': book_infos.split('/')[0],
            # 出版社
            'publisher': book_infos.split('/')[-3],
            # 出版日期
            'date': book_infos.split('/')[-2],
            # 图书价格
            'price': book_infos.split('/')[-1]
        }
# 将抓到的数据（json格式）保存到top250books.txt文件中
def save(content):
    with open('top250books.txt', 'at', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

# 抓取url对应的页面，并将页面内容保存到top250books.txt文件中
def getTop250(url):
    html = getOnePage(url)
    for item in parseOnepage(html):
        print(item)
        save(item)

# 产生10个url
urls= ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]

for url in urls:
    getTop250(url)
