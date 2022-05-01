import time

import requests
from pyquery import PyQuery as pq

def get_one_page(url):
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
        return None
    except Exception:
        return None

def parse_one_page(html):
    doc = pq(html)
    ul = doc('.bigimg')
    liList = ul('li')
    for li in liList.items():
        a = li('a:first-child')
        href = a[0].get('href')
        title = a[0].get('title')
        span = li('.search_now_price')
        price = span[0].text[1:]
        p = li('.search_book_author')
        author = p('a:first-child').attr('title')
        date = p('span:nth-child(2)').text()[1:]
        publisher = p('span:nth-child(3) > a').text()
        comment_number = li('.search_comment_number').text()[:-3]
        detail = li('.detail').text()
        yield {
            'href':href,
            'title':title,
            "price":price,
            'author':author,
            'date':date,
            'publisher':publisher,
            'comment_number':comment_number,
            'detail': detail
        }

if __name__ == '__main__':
    urls = ['http://search.dangdang.com/?key=python&act=input&page_index={}'.format(str(i)) for i in range(1,4)]
    for url in urls:
        book_infos = parse_one_page(get_one_page(url))
        for book_info in book_infos:
            print(book_info)
            time.sleep(1)
