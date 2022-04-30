import urllib.request
from urllib import request
import urllib.error
import socket
from urllib.parse import urlencode,unquote

data = bytes(urllib.parse.urlencode({'name': 'Bill', 'age': 12}), encoding='utf-8')
try:
    response = urllib.request.urlopen('http://httpbin.org/post', data=data, timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('超时')

print('继续工作')
# print(type(response))
# print(response.status,response.msg,response.version)
# print(response.getheaders())
# print(response.getheader('Content-Type'))
# print(response.read().decode('utf-8'))
headers={
    'user-Agent':'hello',
    # 'chinese':urlencode('中国') 错误
}
req = request.Request(url='http://www.baidu.com', data=data, method='POST', headers=headers)
res = urllib.request.urlopen(req)
print(res.read().decode('utf-8'))