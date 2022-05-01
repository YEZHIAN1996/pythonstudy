import xlwt
import requests
import time
from lxml import etree

# 根据指定的页面url获取小说的内容
def getOnePage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)

    infos = selector.xpath('////*[@id="book-img-text"]/ul/li')
    for info in infos:
        yield {
            'title': info.xpath("//div[2]/h2/a/text()")[0],
            'author': info.xpath("//div[2]/p[1]/a[1]/text()")[0],
            'complete': info.xpath("//div[2]/p[1]/span/text()")[0],
            'introduce': info.xpath("//div[2]/p[2]/text()")[0].strip()
        }

header = ['标题', '作者', '完成度', '介绍']
book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('novels')
for h in range(len(header)):
    sheet.write(0, h, header[h])

urls = ['https://www.qidian.com/all/page{}/'.format(str(i) for i in range(1, 11))]
i = 1

for url in urls:
    novels = getOnePage(url)
    for novel in novels:
        print(novel)
        time.sleep(0.1)
        sheet.write(i, 0, novel['title'])
        sheet.write(i, 1, novel['author'])
        sheet.write(i, 2, novel['complete'])
        sheet.write(i, 3, novel['introduce'])
        i += 1

book.save("novels.xls")

