from urllib3 import *

disable_warnings()
http = PoolManager()
url = 'http://localhost:5000'
while True:
    filename = input('请输入需要上传文件的名字(必须在当前目录):')
    if not filename:
        break
    with open(filename, 'rb') as f:
        filedata = f.read()

    response = http.request('POST', url, fields={'file':(filename, filedata)})
    print(response.data.decode('utf-8'))
