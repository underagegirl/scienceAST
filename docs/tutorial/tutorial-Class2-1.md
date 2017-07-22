---
title: Python 基础
---

本节内容可到以下网址自学

* [菜鸟教程](https://www.runoob.com/python/python-tutorial.html)
* [廖雪峰](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)

# 基础数据类型(Number, String , Boolean , Object)
## Number(数值)
python中数字类型分为三种：整型(integers)、浮点型(floating point     numbers)和复数(complex numbers),而复数的实部与虚部都是浮点型。


 operation  | result
---------|----------
 x + y | x 和 y 的总和
 x - y | x 和 y 的差
 x * y | x 和 y 的乘积
 x / y | x 和 y 的商
 x // y | x 除以y的商向下取整的整数
 x % y | 求余数 x / y
 -x | x取负
 +x | x保持不变
 abs(x) | x的绝对值或x的大小
 int(x) | x 转换为整数
 float(x) | x 转化为浮点数
 complex(re， im) | 将参数转化为复数，re为复数的实部，Im为复数的虚部。im 默认为0
 c.conjugate() | c 复数的共轭
 divmod(x， y) | (x // y， x % y)
 pow(x， y) | x的y次幂
 x ** y | x的y次幂
 完整文章请到[官方文档](http://python.usyiyi.cn/translate/python_352/library/stdtypes.html#numeric-types-int-float-complex)查看

需要注意的是：
> 1. 整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的，而浮点数运算则可能会有四舍五入的误差
> 1. 数字类型是不允许改变的，即如果想要改变,必然要重新分配内存空间。

## String(字符串)
关于python字符串的操作与内置方法，可到[菜鸟教程](http://www.runoob.com/python/python-strings.html)进行学习。

## Boolean(布尔值)
布尔是整数的一个子类型,它的返回值为True或者False.

下面是布尔运算:
> 1. x or y(若x为False，则结果为y，否则结果为x)->(1)
> 1. x and y(若x为False，则结果为x，否则结果为y)->(2)
> 1. not x(若x为alse，则结果为True，否则结果为False)->(3)

备注：
> 1. 这是短路运算符，所以如果第一个参数是 False，它就只计算第二个参数.
> 1. 这是短路运算符，所以如果第一个参数是 True，它就只计算第二个参数.
> 1. not 是一个低优先级的布尔运算符，所以 not a == b 解释为 not (a == b)，以及a == not b 是一个语法错误.

## object
python中所有变量都是对象,所有对象都基于object类.

# 基础数据结构(list , tuple , dict)
## list
list是一个可变的序列表，可以随时添加和删除其中的元素，可进行包括索引，切片，加，乘，检查成员等操作,详细信息请参考[菜鸟教程](http://www.runoob.com/python/python-lists.html)进行自学。

注：列表排序的两种方法：
> 1. list.sort()
> 1. sort(list)(python内置方法，毛部长大力推荐的声明式写法)

## tuple
tuple为不可变序列，即一旦被初始化就不能被修改，通常用于储存异构数据的容器，同时也可以对其进行一系列操作，详细信息请参考[菜鸟教程](http://www.runoob.com/python/python-tuples.html)

这里引出可变序列与不可变序列的区别：
> 1. 可变序列是可[hash](http://www.cnblogs.com/sesshoumaru/p/6010180.html)的,相反不可变序列不可hash的。
> 1. 可变序列可以随时进行添加和删除，不可变序列一旦被初始化就不能被修改。

## dict
一个[mapping](http://python.usyiyi.cn/translate/python_352/glossary.html#term-mapping)对象将[hashable](http://python.usyiyi.cn/translate/python_352/glossary.html#term-hashable)的值映射到任意对象,在python中只有dict为标准映射类型。即(key=>value)。

# 控制语句(if,for,while)
## if语句(条件语句)
关于if条件语句可以到[廖雪峰](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431675624710bb20e9734ef343bbb4bd64bcd37d4b52000)与[菜鸟教程](https://www.runoob.com/python/python-if-statement.html)学习

注意：
> 1. 使用if语句时不能忘记":"
> 1. if语言是遵循自上而下判断，即如果if条件成立，后面的判断语句将被忽略

## for循环语句
关于for循环语句可以到[廖雪峰](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431676242561226b32a9ec624505bb8f723d0027b3e7000)与[菜鸟教程](https://www.runoob.com/python/python-for-loop.html)学习

## while循环语句
关于for循环语句可以到[菜鸟教程](https://www.runoob.com/python/python-while-loop.html)学习

注意：
* 无限循环时是`while(True):` 而不是`while(1):`

# 函数与成员访问
## 函数
关于函数调用可以到[廖雪峰](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143167832686474803d3d2b7d4d6499cfd093dc47efcd000)学习，详细信息请参考[官方文档](http://python.usyiyi.cn/translate/python_352/library/functions.html)

例如以下代码：
```python
def sum(a,b):
    return a+b
```
其中`def`是定义函数的关键字，`sum`是函数名，`a,b`是这个函数的参数

其中函数的参数分为：位置参数、默认参数、可变参数、关键字参数。详细信息请到[廖雪峰](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000)进行学习

提示:
* 如果对某个函数的参数不清楚，可用内置`help()`方法在交互式命令行中查看

## 成员访问
例如以下代码：
```python
list = [5,4,3,2,1]
print(list.sort())
```
输出结果为`[1,2,3,4,5]`

这个例子就是访问list处理方法中的`sort()`方法

# 安装和使用第三方库(pip,conda)
## 安装第三方库
* 下载[Anaconda3](https://www.continuum.io/downloads)，选择Python3.6(*64)
* 安装时记得检查是否勾`Add Anaconda to the system PATH encironment variable`这个选项

## 使用第三方库
* 安装完之后，本身Anaconda就自带很多库函数供食用
* 如果想要安装更多有趣的库函数，在cmd命令执行器中输入`pip(conda) install 函数名`即可
* cmd命令执行器打开方式：`win+R`,然后再弹出的窗口中输入`cmd`即可

# 编码与解码
## encode()
以指定的编码格式编码字符串，如
```python
str.encode(encoding='UTF-8')
```
详细信息请到[菜鸟教程](http://www.runoob.com/python/att-string-encode.html)学习
## decode()
以指定的编码格式解码字符串，如
```python
str.decode(encoding='UTF-8')
```
详细信息请到[菜鸟教程](http://www.runoob.com/python/att-string-decode.html)学习

# 任务：自学HTML基础