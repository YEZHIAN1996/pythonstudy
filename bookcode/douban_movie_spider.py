import requests
import re
import sqlite3
import os
import time
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
def get_movie_url(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    movie_hrefs = selector.xpath('//div[@class="hd"]/a/@href')
    print(movie_hrefs)
    for movie_href in movie_hrefs:
        get_movie_info(movie_href)

def get_movie_info(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    try:
        name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')[0]
        director = selector.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')[0]
        actors = selector.xpath('//*[@id="info"]/span[3]/span[2]')[0]
        actor = actors.xpath('string(.)')
        style = re.findall('<span property="v:genre">(.*?)</span>', html.text, re.S)[0]
        country = re.findall('<span class="pl">制片国家 / 地区: </span>(.*?)<br/>', html.text, re.S)[0]
        release_time = re.findall('上映日期:</span>.*?>(.*?)</span>', html.text, re.S)[0]
        time = re.findall('片长:</span>.*?>(.*?)</span>', html.text, re.S)[0]
        score = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')[0]

        global id
        id += 1
        movie = (id, str(name), str(director), str(actor), str(style), str(country), str(release_time), str(time), score)
        print(movie)
        cursor.execute('''insert into movies(name,director,actor,style,country,release_time,time,score)
        values(?,?,?,?,?,?,?,?,?)''', movie)
        conn.commit()
    except IndexError:
        pass

if __name__ == '__main__':
    id = 0
    dbPath = 'movie.sqlite'
    if os.path.exists(dbPath):
        os.remove(dbPath)
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
    cursor.execute('''create table movies
    (id int not null,
    name char(50) not null,
    director char(50) not null,
    actor char(50) not null,
    style char(50) not null,
    country char(50) not null,
    release_time char(50) not null,
    time char(50) not null,
    score real not  null 
    );''')
    conn.commit()
    print('创建数据库成功')
    urls = ['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0, 250, 25)]
    for url in urls:
        get_movie_url(url)
        time.sleep(1)
    conn.close()