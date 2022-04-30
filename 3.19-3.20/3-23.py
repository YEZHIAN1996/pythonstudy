import requests

url = 'https://c.m.163.org/ug/api/wuhan/app/data/list-total?t=329867082220'
response = requests.get(url=url)
json_data = response.json()
# 全国疫情
china_total = json_data['data']['chinaTotal']
print(china_total)
# 全国累计确诊数据