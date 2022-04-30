from urllib3 import *
disable_warnings()

http = PoolManager()
url='http://localhost:5000/register'
response = http.request('POST', url, fields={'name': '李宁', 'age': 18})
for key in response.info().keys():
    print(key, ':', response.info()[key])
data = response.data.decode('utf-8')
print(data)