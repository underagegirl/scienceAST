---
title: Python 基础
---

本节内容可到[网址](http://www.runoob.com/python/python-tutorial.html)或[网址](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/)自学

# 基础数据类型(Number, String , Boolean , Object)
## Number(数值)
python中数字类型分为三种：整型(integers)、浮点型(floating point     numbers)和复数(complex numbers),而复数的实部与虚部都是浮点型。


 operation  | result  |
---------|----------|
 x + y | x 和 y 的总和 |
 x - y | x 和 y 的差 |
 x * y | x 和 y 的乘积 |
 x / y | x 和 y 的商 |
 x // y | x 除以y的商向下取整的整数 |
 x % y | 求余数 x / y |
 -x | x取负 |
 +x | x保持不变 |
 abs(x) | x的绝对值或x的大小 |
 int(x) | x 转换为整数 |
 float(x) | x 转换为浮点数 |
 complex(re， im) | 将参数转化为复数，re为复数的实部，Im为复数的虚部。im 默认为0 |
 c.conjugate() | c 复数的共轭 |
 divmod(x， y) | (x // y， x % y) |
 pow(x， y) | x的y次幂 |
 x ** y | x的y次幂 |
 完整文章请到[官方文档](http://python.usyiyi.cn/translate/python_352/library/stdtypes.html#numeric-types-int-float-complex)查看

需要注意的是：
> 1. 整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的，而浮点数运算则可能会有四舍五入的误差
> 1. 数字类型是不允许改变的，即如果想要改变,必然要重新分配内存空间。

## String(字符串)
用python编写字符串输出时一定要转为'utf-8'格式，因为中文编码超出了ASCII编码的范围，python会报错！

关于python字符串的操作与内置方法，可到这个[网页](http://www.runoob.com/python/python-strings.html)进行学习。

## Boolean(布尔值)
布尔是整数的一个子类型,它的返回值为True或者False.

下面是布尔运算:
> 1. x or y(若x为False，则结果为y，否则结果为x)->(1)
> 1. x and y(若x为False，则结果为x，否则结果为y)->(2)
> 1. not x(若x为alse，则结果为True，否则结果为False)->(3)

备注：
> 2. 这是短路运算符，所以如果第一个参数是 False，它就只计算第二个参数.
> 2. 这是短路运算符，所以如果第一个参数是 True，它就只计算第二个参数.
> 2. not 是一个低优先级的布尔运算符，所以 not a == b 解释为 not (a == b)，以及a == not b 是一个语法错误.

## object
python中所有变量都是对象,所有对象都基于object类.

# 基础数据结构(list , tuple , dict)
## list
list是一个可变的序列表，可以随时添加和删除其中的元素，可进行包括索引，切片，加，乘，检查成员等操作,详细信息请点击此[网址](http://www.runoob.com/python/python-lists.html)进行自学。

注：列表排序的两种方法：
> 1. list.sort()
> 1. sort(list)(python内置方法，毛部长大力推荐的声明式写法)

## tuple
tuple为不可变序列，即一旦被初始化就不能被修改，通常用于储存异构数据的容器，同时也可以对其进行一系列操作，详细信息请点击此[网址](http://www.runoob.com/python/python-tuples.html)

这里引出可变序列与不可变序列的区别：
> 1. 可变序列是可[hash](http://www.cnblogs.com/sesshoumaru/p/6010180.html)的,相反不可变序列不可hash的。
> 1. 可变序列可以随时进行添加和删除，不可变序列一旦被初始化就不能被修改。

## dict
一个[mapping](http://python.usyiyi.cn/translate/python_352/glossary.html#term-mapping)对象将[hashable](http://python.usyiyi.cn/translate/python_352/glossary.html#term-hashable)的值映射到任意对象,在python中只有dict为标准映射类型。即(key=>value)。

# 控制语句(if,for,while)
## if语句(条件语句)
条件语句执行过程图
![picture](http://www.runoob.com/wp-content/uploads/2013/11/if-condition.jpg)

if语句的基本形式
```python
if 判断语句1:
    执行语句
elif 判断语句2:
    执行语句
……
else:
    执行语句
```
多条件判断时可用and和or连接，例如：
```python
num = 9
if num > 0 and num < 9:
    print("1")
elif num < 0 or num > 9:
    print("2")
else:
    print("3")
```
当然其结果为输出 3 .
## 


# 函数调用与成员访问

# 安装和使用第三方库(pip,conda)

# 编码与解码

# 继承关系

# 任务：自学HTML基础