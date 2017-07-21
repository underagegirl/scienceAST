---
title: XPath与CSS 选择器
qrcode: True
---

# XPath与CSS 选择器
与正则表达式不同，XPath和CSS 选择器不是用来处理通用文本的工具。而是针对网页HTML结构进行筛选的工具，两者用法相似但又有所区别。
* XPath 本身是用于处理XML结构文本的工具，因为HTML与XML结构类似，所以亦可处理HTML文本。
* CSS 选择器(CSS Selector) 本身是用于筛选CSS标记的工具，因为现在的网页大多都使用了CSS，所以在处理HTML文本时亦有不错的效果。

关于[XPath](http://www.w3school.com.cn/xpath/xpath_intro.asp)和[CSS 选择器](http://www.w3school.com.cn/cssref/css_selectors.asp)的语法网上已经有不少教程，所以在此就不再赘述。我们主要来看XPath和CSS 选择器在Python中的使用方法。

在本篇中，主要使用到两个第三方库BeautifulSoup和lxml，可以使用pip安装。

# XPath
