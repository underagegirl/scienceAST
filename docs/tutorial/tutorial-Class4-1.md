---
title: 正则表达式
---

# 网页信息提取
在一个网页中包含着很多信息，而我们所需要的往往只是其中的一部分，所以我们在网络上采集信息时，需要对信息进行清洗提取。

常用的方式主要有一下三种：
* 正则表达式
* XPath语句
* CSS选择器

## 正则表达式
>正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑。

以上介绍引自[百度百科](https://baike.baidu.com/item/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F/1700215?fr=aladdin#2)

可以看到，正则表达式就是一种对应规则的过滤。

关于[正则表达式的教程](http://www.runoob.com/regexp/regexp-tutorial.html)网上有许多，这里就不再赘述，我们着重来看正则表达式在Python中的用法。

## re
[re](https://docs.python.org/3/library/re.html)是Python标准库提供的，用于处理正则表达式的库。

### match
`re.match(pattern, string)`

match函数会从`string`的第一字符开始，匹配`pattern`所给出的规则：
* 若在匹配过程中，遇到一个不符合规则的字符，直接结束匹配，并返回None
* 若在匹配过程中，`string`长度小于`pattern`所要求长度，结束匹配过程，并返回None
* 若没有发生上述两种情况，成功匹配完的，则会返回一个包含匹配的字符串以及其在原字符串中的位置信息的对象，不再继续向后匹配。

如以下代码:
``` Python
import re

# 匹配成功
match1 = re.match(r'hello', 'hello world!')
# 匹配失败
match2 = re.match(r'hello world', 'hello')
# 匹配失败
match3 = re.match(r'python', 'hello python')
# 命名分组，匹配成功
match4 = re.match(r'(?P<data>\d{4}-\d{1,2}-\d{1,2}) (\d{2}:\d{1,2}:\d{1,2})', '2017-07-20 11:22:33')

if match1:
    # 可以用成员函数group()来获取所匹配的字符串
    # match1.group()与下一行等价
    print(match1.group(0))
    # 可以用成员函数span()来获取所匹配字符串在原字符串中的起始位置与结束位置
    # match1.span()与下一行等价
    print(match1.span(0))
else:
    print('match1 fail!')

if match2:
    print(match2.group())
else:
    print('match2 fail!')

if match3:
    print(match3.group())
else:
    print('match3 fail!')

if match4:
    # 返回所有分组
    print(match4.groups())
    # 返回所有命名分组
    print(match4.groupdict())
else:
    print('match4 fail!')
```

运行结果:
``` Python
hello
(0, 5)
match2 fail!
match3 fail!
('2017-07-20', '11:22:33')
{'data': '2017-07-20'}
```