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