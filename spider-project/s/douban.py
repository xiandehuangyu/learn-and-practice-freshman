import requests
import json
url = 'https://movie.douban.com/j/chart/top_list?'
param = {
    'type':'24',
    'interval_id':'100:90',
    'action=':"",
    'start':'0',
    'limit':'20',}

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3.1 Safari/605.1.15'
}
response = requests.get(url=url,params=param,headers=headers)
list_data = response.json()
with open('./douban.json','a',encoding='utf-8') as f:
    json.dump(list_data,fp=f,ensure_ascii=False)