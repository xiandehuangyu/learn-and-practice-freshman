import requests

headers29 = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0",
    'Content-Type':'application/json; charset=utfi-8',
    'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIyMDI1MzEwNjE0MjkiLCJjcmVhdGVkIjoxNzc0NDI2OTE5MzgzLCJleHAiOjMzMzEwNDI2OTE5fQ.rstzjFmPS167e3HXX_HANOS9yVzkQVbK5SgWQfCAQKbt1Bly37fQQMSypFSSxXVunLt8VuLsm0OX9ekudj4bkg'
}
headers24 = {
    'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.3.1 Safari/605.1.15",
    'Content-Type':'application/json; charset=utfi-8',
    'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIyMDI1MzEwNjE0MjQiLCJjcmVhdGVkIjoxNzc0NDE5MTUyNTU1LCJleHAiOjMzMzEwNDE5MTUyfQ.irGulbkwsCxsLAaPGY1oLKq7JyZTAdRUF9NK0IvecIx-GhWL_On9dY8JbWQVsqwGfqt6y3i1yPBNzr1as4qFBw'
}
url = 'http://47.120.61.169/punchApi/endPunch'
data1 = {
    "studentID":202531061429,
}
data2 = {
    "studentID":202531061424,
}
#data3 = {
#    "studentID":202531061426,
#}
response1 = requests.post(url=url,json=data1,headers=headers29)
response2 = requests.post(url=url,json=data2,headers=headers24)
#response3 = requests.post(url=url,json=data3,headers=headers)
print(response1.text)
print(response2.text)
#print(response3.text)