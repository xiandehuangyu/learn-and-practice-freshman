import requests

headers29 = {
    'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3.1 Safari/605.1.15",
    'Content-Type':'application/json; charset=utfi-8',
    'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIyMDI1MzEwNjE0MjkiLCJjcmVhdGVkIjoxNzc0MTcyNjc0ODM3LCJleHAiOjMzMzEwMTcyNjc0fQ.Yhrj6ZrGbatn4YgRCa2DDwvLqdXmStlHTL_R8cFZqJ13D5rtf9uIul_3si-AwZ11tFDHzplWzKH86YQJyTMvpg'
}
headers24 = {
    'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3.1 Safari/605.1.15",
    'Content-Type':'application/json; charset=utfi-8',
    'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIyMDI1MzEwNjE0MjQiLCJjcmVhdGVkIjoxNzc0NDE5MTUyNTU1LCJleHAiOjMzMzEwNDE5MTUyfQ.irGulbkwsCxsLAaPGY1oLKq7JyZTAdRUF9NK0IvecIx-GhWL_On9dY8JbWQVsqwGfqt6y3i1yPBNzr1as4qFBw'
}
url = 'http://47.120.61.169/punchApi/startPunch'
data1 = {
    "studentID":202531061424,
}
data2 = {
    "studentID":202531061426,
}
data3 = {
    "studentID":202531061429,
}
url1 = 'http://47.120.61.169/punchApi/login'
data11 = {"studentID":"202531061424","password":"123456"}
data22 = {"studentID":"202531061426","password":"123456"}
data33 = {"studentID":"202531061429","password":"123456"}
response11 = requests.post(url=url1,json=data11,headers=headers24)
#response22 = requests.post(url=url1,json=data22,headers=headers)
response33 = requests.post(url=url1,json=data33,headers=headers29)
response1 = requests.post(url=url,json=data1,headers=headers24)
#response2 = requests.post(url=url,json=data2,headers=headers)
response3 = requests.post(url=url,json=data3,headers=headers29)
print(response1.text)
#print(response2.text)
print(response3.text)