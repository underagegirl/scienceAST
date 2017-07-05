---
title: 网页构成与静态页面爬虫
---
# 静态页面爬虫

首先我们来看下抓取网页的python代码
```
# 导入第三方库requests
import requests

# 抓取github首页
# 使用requests库中提供的get方法
# HTTP请求为GET / HTTP/1.1
# host 为www.github.com
response = requests.get("http://www.github.com")

print('判断是否获取成功')
# 若输出True，则获取数据成功
print(response.ok)
```
至此，我们已经成功获取了