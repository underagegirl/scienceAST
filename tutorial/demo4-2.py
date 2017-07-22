import requests
# 导入lxml中的etree类
from lxml import etree
# 导入BeautifulSoup
from bs4 import BeautifulSoup

# 获取网页信息
r = requests.get('http://news.zol.com.cn/')
# html为包含网页html代码的str对象
html = r.text

# 由HTML创建文档树
selector = etree.HTML(html)
# 使用XPath语句
xpath_result = selector.xpath('//*[@class="content-list-item"]/div/div/a/text()')
# 打印XPath结果
print("Here is the result of xpath:")
for i, item in enumerate(xpath_result):
    print("%-2d: %s" % (i, item))

print('*'*20)

# 由HTML创建soup对象,使用lxml解析器
soup = BeautifulSoup(html, 'lxml')
# 使用CSS 选择器
# select 所返回的为包含bs4.element.Tag的list
css_result = soup.select('.content-list-item > div > div > a')
# 提取Tag的text
css_result_text = [tag.text for tag in css_result]
# 打印CSS Selector结果
print("Here is the result of css selector:")
for i, item in enumerate(css_result_text):
    print("%-2d: %s" % (i, item))
