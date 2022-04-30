from urllib3 import *

disable_warnings()
http = PoolManager(timeout=Timeout(connect=2.0, read=2.0))
url1 = 'http://www.baidu1122.com'
url2 = 'http://httpbin.org/delay/3'
try:
    http.request('GET', url1, timeout=Timeout(connect=2.0, read=4.0))
except Exception as e:
    print(e)
print('____________')
response = http.request('GET', url2, timeout=Timeout(connect=2.0, read=4.0))
print(response.info())
print('------------')
print(response.info()['Content-Length'])
# 会因为读超时报错
response = http.request('GET', url2, timeout=Timeout(connect=2.0, read=2.0))