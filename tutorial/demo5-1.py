import requests
from bs4 import BeautifulSoup
import csv

# 抓取京东活动页面
r = requests.get('https://www.jd.com/moreSubject.aspx')
# 创建soup对象, 指定第三方解析器lxml
soup = BeautifulSoup(r.text, 'lxml')
# 使用CSS Selector筛选元素
items = soup.select('#active_div > ul > li > div > a')
# 提取活动标题以及活动地址
actives = [(i, item.text, item.get('href')) for i, item in enumerate(items)]
# 打开文件
with open('./demo5-1.csv', 'w', encoding='utf-8') as f:
    # 创建CSV写入器
    writer = csv.writer(f)
    # 写入多行数据
    writer.writerows(actives)
