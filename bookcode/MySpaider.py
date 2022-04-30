from urllib3 import *
from re import *

http = PoolManager()
disable_warnings()
# 下载html文件
def download(url):
    result = http.request('GET', url)
    # 将下载的html文件代码用utf-8格式解码成字符串
    htmlStr = result.data.decode('utf-8')
    # 输出当前抓取的html代码
    print(htmlStr)
    return htmlStr
# 分析html代码
def analyse(htmlStr):
    # 利用正则表达式获取所有的a节点
    aList = findall('<a[^>]*>', htmlStr)
    result = []
    # 对a节点列表进行迭代
    for a in aList:
        # 利用正则表达式从a节点提取herf属性的值
        g = search('href[\s]*=[\s]*[\'"]([^>\'""]*)[\'"]', a)
        if g != None:
            # 获取a节点的属性值，herf属性值就是第一个分组的值
            url = g.group(1)
            # 将url编程绝对链接
            url = 'http://localhost/files/'+url
            # 将提取出的url追加到result列表中
            result.append(url)
    return result
# 用于从入口点抓取html文件的函数
def crawler(url):
    # 输出正在抓取的url
    print(url)
    # 下载html文件
    html = download(url)
    # 分析html代码
    urls = analyse(html)
    # 对每一个url递归调用crawler函数
    for url in urls:
        crawler(url)
#  从入口函数开始抓取所有的html
crawler('http://localhost/files')