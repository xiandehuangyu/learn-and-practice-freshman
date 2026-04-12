
import json

import requests

# 1. 定义请求头（包含鉴权Token和Content-Type）
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3.1 Safari/605.1.15",
    'Content-Type': 'application/json; charset=utf-8',
    # 关键：添加鉴权Token
    'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIyMDI1MzEwNjE0MjkiLCJjcmVhdGVkIjoxNzc0MTcyNjc0ODM3LCJleHAiOjMzMzEwMTcyNjc0fQ.Yhrj6ZrGbatn4YgRCa2DDwvLqdXmStlHTL_R8cFZqJ13D5rtf9uIul_3si-AwZ11tFDHzplWzKH86YQJyTMvpg'
}

# 2. 接口地址
url = 'http://47.120.61.169/punchApi/startPunch'

# 3. 请求数据
data = {
    "studentID": 202531061429
}

try:
    # 4. 发送POST请求（使用json参数自动序列化，或用data=json.dumps(data)）
    # 方式1（推荐）：使用json参数
    response = requests.post(url=url, json=data, headers=headers)
    
    # 方式2：手动序列化（效果同上）
    # response = requests.post(url=url, data=json.dumps(data), headers=headers)
    
    # 5. 打印响应结果
    print("响应状态码:", response.status_code)
    print("响应内容:", response.text)
    
    # 如果返回的是JSON格式，也可以直接解析
    if response.status_code == 200:
        result = response.json()
        print("解析后的JSON数据:", result)
        
except requests.exceptions.RequestException as e:
    print("请求出错:", str(e))