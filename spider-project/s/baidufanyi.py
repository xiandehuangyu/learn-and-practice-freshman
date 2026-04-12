import requests
import json
headers = {
    'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3.1 Safari/605.1.15"

}
url = 'https://fanyi.baidu.com/sug'
kw = input("你想搜的什么单词:")
data = {
    "kw":kw
}
response = requests.post(url=url,data=data,headers=headers)
page_text = response.json()
with open('ci.json','a',encoding='utf-8') as f:
    json.dump(page_text,fp=f,ensure_ascii=False)