from urllib3 import request, disable_warnings, PoolManager
from urllib.parse import urlencode

disable_warnings()
http = PoolManager()

# url 组合
# url = 'http://www.baidu.com/s?' + urlencode({'wd':'极客起源'})
# response = http.request('GET', url)
# print(url)

url = 'http://www.baidu.com/s'
response = http.request('GET', url, fields={'wd':'极客起源'})
data = response.data.decode('utf-8')
print(data)