import requests
from pyquery import PyQuery as pq
html = '''
<div id="panel">
    <ul class="list1">
        <li class="item1" value1="1234" value2 = "hello world"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item"><a href="https://www.jd.com"> 京东商城</a></li>        
    </ul>
    <ul class="list2">
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item" ><a href="https://www.microsoft.com">微软</a></li>
        <li class="item2"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>
'''
doc = pq(html)
result = doc('#panel .list1')
print(type(result))
print(result)
print(result('.item'))
print(result('a')[1].get('href'), result('a')[1].text)
print()

doc = pq(requests.get('https://www.jd.com').text)
group1 = doc('#navitems-group1')
print(group1('a')[0].text, group1('a')[1].text, group1('a')[2].text, group1('a')[3].text)
group2 = doc('#navitems-group2')
print(group2('a')[0].text, group2('a')[1].text, group2('a')[2].text, group2('a')[3].text)
group3 = doc('#navitems-group3')
print(group3('a')[0].text, group3('a')[1].text)
