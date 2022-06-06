import requests
from lxml import etree
import pymongo
from queue import Queue
import threading

def handle_request(url):
    '''
    发送url请求
    :param url:
    :return: resposne.text
    '''
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Host": "movie.douban.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    response = requests.get(url=url, headers=header, timeout=(5, 5), proxies=None)
    if response.status_code == 200 and response:
        return response.text


class PageSpider(threading.Thread):
    '''
    页码请求，获取各详情页的页码，将其插入详情页url队列
    '''
    def __init__(self, thread_name, page_url_queue, detail_page_url_queue):
        super(PageSpider, self).__init__()
        self.thread_name = thread_name
        self.page_url_queue = page_url_queue
        self.detail_page_url_queue = detail_page_url_queue

    def parse_detail_page_url(self, content):
        '''
        解析页面，将详情页的url插入详情页队列
        :param content:
        :return:
        '''
        html = etree.HTML(content)
        detail_page_urls = html.xpath('//div[@class="article"]/ol/li/div[@class="item"]/div[@class="pic"]/a/@href')
        for detail_page_url in detail_page_urls:
            self.detail_page_url_queue.put(detail_page_url)

    def run(self):
        print('{}启动'.format(self.thread_name))
        try:
            while not self.page_url_queue.empty():
                url = self.page_url_queue.get(block=False)
                page_response = handle_request(url)
                if page_response:
                    self.parse_detail_page_url(content=page_response)
        except Exception as e:
            print('{} run error:{}'.format(self.thread_name, e))
        print('{} end'.format(self.thread_name))

class DetailPageSpider(threading.Thread):
    '''
    从详情页url队列中取出url，请求详情页并将数据插入到数据队列
    '''
    def __init__(self, thread_name, detail_page_url_queue, data_queue):
        super(DetailPageSpider, self).__init__()
        self.thread_name = thread_name
        self.detail_page_url_queue = detail_page_url_queue
        self.data_queue = data_queue

    def run(self):
        print('{} 启动'.format(self.thread_name))
        try:
            while not self.detail_page_url_queue.empty():
                url = self.detail_page_url_queue.get(block=False)
                detail_page_response = handle_request(url=url)
                if detail_page_response:
                    self.data_queue.put(detail_page_response)
        except Exception as e:
            print('{} run error:{}'.format(self.thread_name, e))
        print('{} end'.format(self.thread_name))

class DataSpider(threading.Thread):
    '''
    从数据队列取出数据并解析，将其插入到mongo数据库
    '''
    def __init__(self, thread_name, data_queue, mongo, lock):
        super(DataSpider, self).__init__()
        self.thread_name = thread_name
        self.data_queue = data_queue
        self.mongo = mongo
        self.lock = lock

    def _join_list(self, item):
        return ''.join(item)

    def parse(self, data):
        html = etree.HTML(data)
        info = {
            # 解析电影名称、演职人员、电影评分、评价人数、电影简述信息
            'movie_name': self._join_list(html.xpath('//div[@id="content"]/h1/span[1]/text()')),
            'actor_name': self._join_list(html.xpath('//span[@class="actor"]/span[2]')),
            'grade': self._join_list(html.xpath('//div[@id="interest_sectl"]/div/div[2]/strong/text()')),
            'rating_sum': self._join_list(html.xpath('//div[@id="interest_sectl"]/div/div[2]/div[@class="rating_right"]/div[2]/a/span/text()')),
            'simple_info': self._join_list(html.xpath('//span[@class="short"]/span/text()'))
        }

        with self.lock:
            self.mongo.insert_one(info)
        print(info)

    def run(self):
        print('{} 启动'.format(self.thread_name))
        try:
            while not self.data_queue.empty():
                detail_page_data_response = self.data_queue.get(block=False)
                self.parse(data=detail_page_data_response)
        except Exception as e:
            print('{} run error:{}'.format(self.thread_name, e))
        print('{} end'.format(self.thread_name))

def main():
    # 页码url队列
    page_url_queue = Queue()
    # 详情页url队列
    detail_page_url_queue = Queue()
    # 数据队列
    data_queue = Queue()

    for i in range(0, 266, 25):
        url = 'https://movie.douban.com/top250?start={}'.format(i)
        page_url_queue.put(url)

    page_spider_thread_name_list = ['列表页采集1号', '列表页采集2号', '列表页采集3号']
    page_spider_list = []
    for page_spider_thread_name in page_spider_thread_name_list:
        thread = PageSpider(page_spider_thread_name, page_url_queue, detail_page_url_queue)
        thread.start()
        page_spider_list.append(thread)
    while not page_url_queue.empty():
        pass
    for thread in page_spider_list:
        if thread.is_alive():
            thread.join()

    detail_page_thread_name_list = ['详情页采集1号', '详情页采集2号', '详情页采集3号', '详情页采集4号', '详情页采集5号']
    detail_page_list = []
    for detail_page_thread_name in detail_page_thread_name_list:
        thread = DetailPageSpider(detail_page_thread_name, detail_page_url_queue, data_queue)
        thread.start()
        detail_page_list.append(thread)
    while not detail_page_url_queue.empty():
        pass
    for thread in detail_page_list:
        if thread.is_alive():
            thread.join()

    lock = threading.Lock()
    # 数据存入mongo
    myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    mydb = myclient['douban_movie']
    mycollection = mydb['douban_movie_info']

    data_thread_name_list = ['数据处理1号', '数据处理2号', '数据处理3号']
    data_list = []
    for data_thread_name in data_thread_name_list:
        thread = DataSpider(data_thread_name, data_queue, mycollection, lock)
        thread.start()
        data_list.append(thread)
    while not data_queue.empty():
        pass
    for thread in data_list:
        if thread.is_alive():
            thread.join()

if __name__ == '__main__':
    main()