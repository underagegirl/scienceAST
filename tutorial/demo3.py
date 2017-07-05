import requests

# 抓取github首页
response = requests.get("http://www.github.com")

print('输出HTTP Status Code')
print(response.status_code)

print('输出网页的编码格式')
print(response.encoding)

print('输出Request的Headers')
print(response.request.headers)

print('输出Response的Headsers(由服务器返回)')
print(response.headers)

print('输出网页的内容')
print(response.content)

print('输出网页的HTML代码')
print(response.text)
