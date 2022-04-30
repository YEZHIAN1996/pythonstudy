import requests
from lxml import etree

r = requests.get('http://www.jd.com')
parser = etree.HTMLParser()
html = etree.HTML(r.text)

nodes = html.xpath('//*[@id="navitems-group1"]//a/text()')
print(nodes)

nodes = html.xpath('//*[@id="navitems-group2"]//a/text()')
print(nodes)

nodes = html.xpath('//*[@id="navitems-group3"]//a/text()')
print(nodes)

