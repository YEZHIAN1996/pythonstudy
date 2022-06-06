import requests
from lxml import etree
import pymongo
from queue import Queue
import threading

def handle_request(url):
    '''
    :param url:
    :return: response.text
    '''
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
    }
    # 发送请求
    response = requests.get(url=url, headers=headers, timeout=(5, 5), proxies=None)
    if response.status_code == 200 and response:
        return response.text

class PageSpider(threading.Thread):
    '''
        页码url请求多线程
    '''
    def __init__(self, thread_name, page_queue, detail_queue):
        super(PageSpider, self).__init__()
        self.thread_name = thread_name
        self.page_queue = page_queue
        self.detail_queue = detail_queue

    def parse_detail_page(self, content):
        '''
        处理page_url返回数据，解析电影详情页的url
        :param content: page_response.text
        :return: detail_url, self.detail.queue
        '''
        # 将页码返回数据实例化
        item_html = etree.HTML(content)
        # 解析出所有详情页的url
        detail_urls = item_html.xpath('//a[@class="thumbnail"]/@href')
        for detail_url in detail_urls:
            # 将详情页的url放入详情页队列
            self.detail_queue.put(detail_url)

    def run(self):
        # 实际发送请求,请求页码url
        print('{}启动'.format(self.thread_name))
        # 不断从页码队列取url，并发送请求，当队列为空时停止
        try:
            while not self.page_queue.empty():
                # 从Queue中获取数据，并设置为非阻塞状态
                page_url = self.page_queue.get(block=False)
                page_response = handle_request(url=page_url)
                if page_response:
                    # 解析每页30条的url
                    self.parse_detail_page(content=page_response)
        except Exception as e:
            print('{} run error: {}'.format(self.thread_name, e))
        print('{} 结束'.format(self.thread_name))


class DetailSpider(threading.Thread):
    '''
        多线程请求详情页
    '''
    def __init__(self, thread_name, detail_queue, data_queue):
        super(DetailSpider, self).__init__()
        self.thread_name = thread_name
        self.detail_queue = detail_queue
        self.data_queue = data_queue

    def run(self):
        # 实际发送请求,请求页码url
        print('{}启动'.format(self.thread_name))
        # 不断从页码队列取url，并发送请求，当队列为空时停止
        try:
            while not self.detail_queue.empty():
                # 从Queue中获取数据，并设置为非阻塞状态
                detail_url = self.detail_queue.get(block=False)
                detail_response = handle_request(url=detail_url)
                if detail_response:
                    # 请求的详情页数据放入到data_queue里面去
                    self.data_queue.put(detail_response)
        except Exception as e:
            print('{} run error: {}'.format(self.thread_name, e))
        print('{} 结束'.format(self.thread_name))

class DataParse(threading.Thread):
    '''
        详情页数据处理
    '''
    def __init__(self, thread_name, data_queue, mongo, lock):
        super(DataParse, self).__init__()
        self.thread_name = thread_name
        self.data_queue = data_queue
        self.mongo = mongo
        self.lock = lock

    def _join_list(self, item):
        # 专门处理列表的
        return ''.join(item)

    def parse(self, data):
        '''
        解析 data_queue 里面的数据
        :param data: data_queue.get()
        :return: pymongo
        '''
        # 实例化
        html = etree.HTML(data)
        info = {
            'title': self._join_list(html.xpath('//div["page-header"]/h1/text()')),
            'update_time': self._join_list(html.xpath('//div[@class="panel-body"]/p[1]/text()')),
            'type': self._join_list(html.xpath('//div[@class="panel-body"]/p[2]/text()')),
            'starring': self._join_list(html.xpath('//div[@class="panel-body"]/p[3]/text()')),
            'desc': self._join_list(html.xpath('//div[@class="panel-body"]/p[4]/text()')),
            'download_url': self._join_list(html.xpath('//div[@class="panel-body"]/p[5]/text()')),
            'source_url': self._join_list(html.xpath('//div[@class="panel-body"]/p/a/@href'))
        }
        # 由于是多线程并发，所有引入锁进行控制
        with self.lock:
            self.mongo.insert_one(info)
        print(info)

    def run(self):
        # 实际发送请求,请求页码url
        print('{}启动'.format(self.thread_name))
        # 不断从页码队列取url，并发送请求，当队列为空时停止
        try:
            while not self.data_queue.empty():
                # 从Queue中获取数据，并设置为非阻塞状态
                detail_info = self.data_queue.get(block=False)
                # 用xpath解析
                self.parse(detail_info)
        except Exception as e:
            print('{} run error: {}'.format(self.thread_name, e))
        print('{} 结束'.format(self.thread_name))

def main():
    # 页码队列
    page_queue = Queue()
    for i in range(1, 36):
        url = 'http://movie.54php.cn/movie/?&p={}'.format(i)
        page_queue.put(url)
    # 电影url队列
    detail_queue = Queue()
    # 详情页队列
    data_queue = Queue()
    page_spider_threadname_list = ['列表页采集1号', '列表页采集2号', '列表页采集3号']
    page_spider_list = []
    for thread_name in page_spider_threadname_list:
        thread = PageSpider(thread_name=thread_name, page_queue=page_queue, detail_queue=detail_queue)
        # 启动线程
        thread.start()
        page_spider_list.append(thread)

    # 查看当前的page_queue里面的数据状态
    while not page_queue.empty():
        # 有数据什么都不干
        pass
    # 释放资源
    for thread in page_spider_list:
        if thread.is_alive():
            thread.join()

    detail_spider_threadname_list = ['详情页采集1号', '详情页采集2号', '详情页采集3号', '详情页采集4号', '详情页采集5号']
    detail_spider_list = []
    for thread_name in detail_spider_threadname_list:
        thread = DetailSpider(thread_name=thread_name, detail_queue=detail_queue, data_queue=data_queue)
        # 启动线程
        thread.start()
        detail_spider_list.append(thread)

    # 查看当前的detail_queue里面的数据状态
    while not detail_queue.empty():
        # 有数据什么都不干
        pass
    # 释放资源
    for thread in detail_spider_list:
        if thread.is_alive():
            thread.join()

    # 在这里能看到90条数据
    # print(detail_queue.qsize())
    # 在这里能看到90条数据
    # print(data_queue.qsize())

    # 使用lock，要向mongo插入数据
    lock = threading.Lock()
    # 数据存入mongo
    myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    mydb = myclient['db_movie']
    mycollection = mydb['movie_info']

    # 启动多线程，处理数据
    data_parse_threadname_list = ['数据处理线程1号', '数据处理线程2号', '数据处理线程3号', '数据处理线程4号', '数据处理线程5号']
    data_parse_list = []
    for thread_name in data_parse_threadname_list:
        thread = DataParse(thread_name=thread_name, data_queue=data_queue, mongo=mycollection, lock=lock)
        # 启动线程
        thread.start()
        data_parse_list.append(thread)

    # 查看当前的data_queue里面的数据状态
    while not data_queue.empty():
        # 有数据什么都不干
        pass
    # 释放资源
    for thread in data_parse_list:
        if thread.is_alive():
            thread.join()

if __name__ == '__main__':
    main()