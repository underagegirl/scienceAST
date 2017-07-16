---
title: Python 基础
---

本篇部分代码参考自《Natural Language Processing with Python》

# 引用对象的赋值
请考虑下列代码运行结果
``` Python
empty = []
nested = [empty, empty, empty]
empty.append('1')
print(nested)
```
正常结果为：`[['1'], ['1'], ['1']]`

## 解释
可以使用内建的id函数来查看对象的标识符
``` Python
empty = []
nested = [empty, empty, empty]
print(id(empty))
print([id(item) for item in nested])
# 输出结果为
# 2442757933960
# [2442757933960, 2442757933960, 2442757933960]
```

可以看到nested中的三个元素均指向empty对象， 所以在对empty对象进行修改后，nested中元素的值也会相应的改变。

## 思考
以下三种操作有什么不同
``` Python
l = ['1', '2', '3']
# Operation 1
l1 = l
# Operation 2
l2 = l[:]
# Operation 3
import copy
l3 = copy.deepcopy(l)
```

# 判断相等
请分析以下代码中的三种判断区别
``` Python
list1 = ['1']
list2 = ['1']
# Operation 1
print(list1 == list2)
# Operation 2
print(list1 is list2)
# Operation 3
print(isinstance(list1, list))
```
正确输出结果为：
``` Python
True
False
True
```

## 解释
上述代码中的三种判断作用分别如下：
1. 判断list1和list2值是否相等
2. 判断list1与list2是否引用同一个对象
3. 判断list1是否为list类的一个实例

# 列表生成式与产生器表达式
请解决以下问题：
> 输出list1中最长的字符串
``` Python
list1 = ['Beautiful', 'is', 'better', 'than', 'ugly', '.', 'Explicit', 'is', 'better', 'than', 'implicit', '.', 'Simple', 'is', 'better', 'than', 'complex']
```

实现一
``` Python
longest = ''
for item in list1:
    if len(item) > len(longest):
        longest = item

print(longest)
```

实现二
``` Python
maxlen = max(len(item) for item in list1)
print([item for item in list1 if len(item) == maxlen])
```

运行后可以发现， 这两种实现都可以达到任务要求，但显然后一种实现更贴近人的思维。