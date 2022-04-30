from urllib3 import *
from re import *
http = PoolManager()
# 禁止显示警告信息
disable_warnings()
def download(url):
    result = http.request('GET', url)
    # 将下载的html文件代码用utf-8格式解码成字符串
    htmlStr = result.data.decode('utf-8')
    # 输出当前抓取的html代码
    # print(htmlStr)
    return htmlStr
# 分析html代码
def analyse(htmlStr):
    # 利用正则表达式获取所有的class属性值为post-item-title节点
    aList = findall('<a[^>]*post-item-title[^>]*>[^<]*</a>', htmlStr)
    result = []
    # 对a节点列表进行迭代
    for a in aList:
        # 利用正则表达式从a节点提取herf属性的值
        g = search('href[\s]*=[\s]*[\'"]([^>\'""]*)[\'"]', a)
        if g != None:
            url = g.group(1)
            # 通过查找的方式提取a节点中博客的标题
        index1 = a.find(">")
        index2 = a.rfind("<")
        # 获取博客标题
        title = a[index1+1:index2]
        d = {}
        d['url'] = url
        d['title'] = title
        result.append(d)
    return result

def crawler(url):
    html = download(url)
    blogList = analyse(html)
    for blog in blogList:
        print("title:", blog['title'])
        print("url:", blog['url'])

crawler('https://www.cnblogs.com')

