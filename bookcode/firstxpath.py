from lxml import etree

parser = etree.HTMLParser()
tree = etree.parse('test.html', parser)
# nodes = tree.xpath("//a[@href='https://www.jd.com']")
nodes = tree.xpath("//a[contains(@href,'www')]")
print(len(nodes))
for i in range(0, len(nodes)):
    print(nodes[i].text)


urls = nodes = tree.xpath("//a[contains(@href,'www')]/@href")
for i in range(0,len(urls)):
    print(urls[i])
# html = '''
#     <div>
#         <li class=''item1><a href='https://www.baidu.com'>baidu</a></li>
#         <li class=''item2><a href='https://www.jd.com'>jd</a></li>
#         <li class=''item3><a href='https://www.taobao.com'>taobao</a></li>
#     </div>
# '''
#
# tree = etree.HTML(html)
# aTags = tree.xpath("//li[@class='item2']")
# if len(aTags) > 0:
#     print(aTags[0][0].get('href'), aTags[0][0].text)

