import requests

# url='http://httpbin.org/ip'
# r = requests.get(url)
# print(r.text)
# r2 = requests.post('http://httpbin.org/post',data={'name':'imooc'})
# print(r2.text)
# 获取图片
# r3 = requests.get('http://www.imooc.com/static/img/index/logo.png')
# with open('imooc.png', 'wb') as f:
#     f.write(r.content)

# json
# print(r.json())

# 响应码
# print(r.status_code)

r4 = requests.get('http://httpbin.org/headers')
print(r4.headers)