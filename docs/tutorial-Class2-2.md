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
