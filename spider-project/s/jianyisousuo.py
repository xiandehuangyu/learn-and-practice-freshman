import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3.1 Safari/605.1.15'
}
url = 'https://www.sogou.com/web'
kw = input("输入你想搜的:")
param = {
    'query':kw
}
response = requests.get(url=url,params=param,headers=headers)
page_text = response.text
fileName = kw + '.html'
with open(fileName,'w',encoding='utf-8') as fp:
    fp.write(page_text)
print("OK")