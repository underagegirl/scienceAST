---
title: Python学习笔记
description: 隔壁老王
---

## dict和set
### dict
* 1

    输入d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}  
　　d['Michael']

    输出　95

* 2

    输入d['Adam'] = 67  
    输入d['Adam']

    输出67

* 3

    dict中一个key只能对应一个value

* 4

    用in判断key是否存在

    例如：输入'Thomas' in d

    输出False

* 5

    要删除一个key，用pop(key)方法，对应的value也会从dict中删除(是删除key,不是删除value)

    例如：d.pop('Bob')

* 6

    从dict中可以用get函数(get是成员函数)

    例如：输入  
    d = {'a':2}  
    d.get('b')  
    d.get('a')

    输出　None  1

### set
* 1

    set和dict类似，也是一组key的集合，但不存储value。在set中没有重复的key(key不重复)

* 2

    要创建一个set，需要提供一个list作为输入集合

    例如：s = set([1,2,3])
    s
    {1,2,3}

* 3

    重复元素在set中自动被过滤

* 4

    add(key)方法可以添加元素到set中

    例如：输入  
    s = set([1,2,3])  
    s.add(4)   
    s   
    输出  
    {1,2,3,4}

    添加重复的没有效果

* 5

    remove(key)用于删除元素，用法与get一样

* 6

    两个set可做数学意义上的交集，并集等操作

    例如：输入  
    s1 = set([1,2,3])  
    s2 = set([2,3,4])   
    s1 & s2  
    输出  
    {2,3}  
    输入  
    s1 | s2  
    输出  
    {1,2,3,4}

### 可变和不可变对象
* 1

    list可变，对list进行改变list变化，而对不可变对象例如str进行替换原str不变

## 函数
### 调用函数
* 1

    函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
    例如：a = abs
    a(-1)
    1

* 2

    数据类型转换

    **input:   int('123')**

    output:  123

    **input:   int(12.34)**

    output:  12

    **input:   float('12.34')**

    output:  12.34

    **input:   str(1.23)**

    output:  '1.23'

    **input:   str(100)**

    output:  '100'

    **input:   bool(1)**

    output:  True

    **input:   bool('')**

    output:  False

### 递归函数
* 1

    在一个函数内部调用自身，这个函数就是递归函数
    例如：计算阶乘
    def fact(n):  
    　　if n == 1:  
    　　　　 return 1  
    　　return n * fact(n-1)  
    可能栈溢出
    进行尾递归优化  
    def fact(n):  
    　　return fact_iter(n, 1)

    def fact_iter(num, product)  
　　　　　if num == 1:  
    　　　　　　　return product  
　　　　　return fact_iter(num - 1, num * product)

## 高级特性
### 切片
* 1
    
    切片是左闭右开的
    切片格式：L[start: stop: step]

    输入L = list(range(100))
    输入L
    输出[0, 1, 2, 3, ..., 99]

    例子：
    L[:10]

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  功能：输出前10个数

    L[-10:]

    [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]  功能：输出后10个数

    L[10:20]

    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]  功能：输出前11-20个数

    L[:10:2]

    [0, 2, 4, 6, 8]  功能：输出隔几个步长的数

    L[:]

    [0, 1, 2, 3, ..., 99]   功能：原样输出

* 2
    
    字符串进行切片
    例如：  
    input:   'ABCDEFG'[:3]

    output:  'ABC'

    input:   'ABCDEFG'[::2]

    output:  'ACEG'

### 迭代
* 1

    定义：给定一个list或tuple，通过for循环来遍历这个list或tuple，这种遍历成为迭代。在Python中，迭代通过for......in来实现。只要是可迭代对象均可进行迭代，并非一定是list或tuple。

    例如：
    ①dict也可迭代

    input:   d = {'a': 1, 'b': 2, 'c': 3}

        for key in d:
    ...     print(key)

    output:  
    a
    
    b
    
    c

    默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()

    ②字符串可迭代

    input:   
    for ch in 'ABC':  
    　　print(ch)   

    output:

    A

    B

    C

* 2
    
    在for循环里，可以引用两个变量，这在Python里十分常见，例如：

    input:  
    for x, y in [(1, 1), (2, 4), (3, 9)]:  
    　　print(x, y)

    output:

    1　　1

    2　　4

    3　　9

### 列表生成式
* 1

    用于创建list的生成式

    例如：

    ①要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))

    input:   list(range(1, 11))

    output:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    ②用循环生成[1x1, 2x2, 3x3, ..., 10x10]

    input:  

    l = []

    for x in range(1, 11):
    
    ...    l.append(x * x)

    l

    output:

    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    ③用列表生成式生成②的结果

    input:  [x*x for x in range(1, 11)]

    output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    ④

    input:  [x * x for x in range(1, 11) if x % 2 == 0]

    output: [4, 16, 36, 64, 100]

    ⑤利用两层循环生成全排列
    
    input:   [m + n for m in 'ABC' for n in 'XYZ']

    output:  ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

* 2

    列表生成式也可以使用两个变量来生成list

    例如:

    input:  

    d = {'x': 'A', 'y': 'B', 'z': 'C' }

    [k + '=' + v for k, v in d.items()]

    output:

    ['y=B', 'x=A', 'z=C']

* 3

    把一个list中所有的字符串变成小写

    input:

    L = ['Hello', 'World', 'IBM', 'Apple']

    [s.lower() for s in L]

    output:

    ['hello', 'world', 'ibm', 'apple']

### 生成器
* 1

    生成器：generator是一种一边循环一边生成的机制，不必创建完整的list，从而节省大量的空间

    创建一个generator可以将一个列表生成式的[]改为(),例如：

    input:  g = (x * x for x in range(10))

    input:  g

    output: <generator object <genexpr> at 0x1022ef630>

    可以利用next()函数打印generator中的每一个元素，例如：

    input:  
    next(g)  
    output: 0  
    input:    
    next(g)  
    output: 1

    但使用next函数过于麻烦，因此可以用for循环来解决问题。例如：

    input:    
    　　　　　g = (x * x for x in range(10))  
    　　　　　for n in g:  
    　　　　　　　　　print(n)
    
    output:   
    0  
    1  
    4  
    9  
    16  
    25  
    36  
    49  
    64  
    81

* 2

    用函数打印斐波那契数列

    def fib(max):  
   　　　　　n, a, b = 0, 0, 1  
   　　　　　while n < max:  
   　　　　　　　print(b)  
   　　　　　　　a, b = b, a + b  
   　　　　　　　n = n + 1  
   　　　　　return 'done'

    将该函数变为generator，只需将print(b)改为yield(b),如下：  
    def fib(max):  
    n, a, b = 0, 0, 1  
    while n < max:  
        yield b  
        a, b = b, a + b  
        n = n + 1  
    return 'done'

    这是**定义generator的另一种方法**，如果一个函数定义中包含yield关键字，那么这就不再是一个普通函数而是一个generator

* 3

    函数和generator的区别。函数是顺序执行，遇到return语句或者最后一行函数就返回。而变为generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

### 迭代器
* 1

    list、tuple、dict、set、str这类集合数据类型和generator包括生成器和带yield的generator function均可以直接作用于for循环。这些可以直接作用于for循环的**对象**称为可迭代对象：Iterable

    use isinstance() to judge whether a object is a Iterable or not.

    for example:

    from collections import Iterable
    isinstance([], Iterable)  
    True  
    isinstance({}, Iterable)  
    True  
    isinstance('abc', Iterable)  
    True  
    isinstance((x for x in range(10)), Iterable)  
    True  
    isinstance(100, Iterable)  
    False  

* 2

    可以被next()函数调用并不断返回下一个值的**对象**称为迭代器：Iterator
    
    可以使用isinstance()判断一个对象是否是Iterator对象,for example:

        from collections import Iterator  
    isinstance((x for x in range(10)), Iterator)  
    True  
    isinstance([], Iterator)  
    False  
    isinstance({}, Iterator)  
    False  
    isinstance('abc', Iterator)  
    False

    生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator

    为什么list、dict、str等数据类型不是Iterator？

    因为Python的Iterator对象表示的是一个数据流,Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

    Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

## 函数式编程
### 高阶函数(Higher-order function)
* 1

    **变量可以指向函数**  
    例如:  
    input:  
    x = abs(-10)  
    x  
    output:   
    10

    input:  
    f = abs  
    f(-10)  
    output:  
    10

* 2

    **函数名也是变量**  
    例如：  
    input:  
    abs = 10  
    abs(-10)  
    output:  
    Traceback (most recent call last):  
    File "<stdin>", line 1, in <module>  
    TypeError: 'int' object is not callable
    
    因为abs这个变量已经不指向求绝对值函数而是指向一个整数10

* 3

    **传入函数**  
    一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数，例如:  
    input:  
    def add(x, y, f):  
    　　return f(x)+f(y)

### map/reduce
1. 

[Google](http://research.google.com/archive/mapreduce.html)
如果感兴趣可以通过Google的这篇论文来大概明白map和reduce的概念

2.  
map(func, *iterables),map后有两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回,例如：  
input:  
def f(x):  
　　　return x * x  
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])  
list(r)  
output:  
[1, 4, 9, 16, 25, 36, 49, 64, 81]

map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x^2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串，例如：  
input:  
list(map(str,[1,2,3,4,5,6,7,8,9]))  
output:  
['1', '2', '3', '4', '5', '6', '7', '8', '9']

3. 
reduce(function, sequence[, initial]),reduced的参数需要一个**具有两个参数的函数**和一个序列。  
reduce把结果继续和序列的下一个元素做累积计算，其效果就是：  
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)  
使用reduce时要导入：from functools import reduce  
reduce应用举例:

将序列[1, 2, 3, 4, 5]变为整数12345   
input:   
def fn(x, y):  
　　return x*10+y  

reduce(fn, [1, 2, 3, 4, 5])  
output:  
12345

考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数:  
from functools import reduce

def str2int(s):  
　　def fn(x, y):  
　　　　return x * 10 + y  
　　def char2num(s):  
　　　　return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]  
　　return reduce(fn, map(char2num, s))  
以上代码可用lambdah函数进行简化：  
from functools import reduce

def char2num(s):  
　　return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]  

def str2int(s):  
　　return reduce(lambda x, y: x * 10 + y, map(char2num, s))  
以上代码和int等效 

### filter
1.  
filter()函数用于过滤序列，和map()类似，filter()也接收**一个函数和一个序列**。和map()不同的是，filter()把传入的函数依次作用于**每个元素**，然后根据返回值是True还是False决定保留还是丢弃该元素。

2. 在一个list中删除偶数只保留奇数，实现方法如下:  
input:  
def is_odd(n):  
　　return n % 2 == 1

list(filter(is_odd, [1, 5, 9, 6, 3, 7 , 8, 14]))  
output:  
[1, 5, 9, 3, 7]

3.   
用filter求素数，实现代码如下:  
*用于生成一个无限的奇数列*   
def odd_iter():  
　　n = 1  
　　while True:  
　　　　n = n + 2  
　　　　yield n

*一个用于过滤不被之前奇数整除的新奇数*  
def not_divisible(n):  
　　return lambda x: x % n > 0  

*查找素数函数*  
def primes():  
　　yield 2  
　　it = _odd_iter()  
　　while True:  
　　　　n = next(it)  
　　　　yield n  
　　　　it = filter(_not_divisible(n), it)  

*设定限制*  
for n in primes():  
　　if n < 1000:  
　　　　print(n)  
　　else:  
　　　　break

### sorted
1. 
Python内置的sorted()函数就可以对list进行排序：
input:
sorted([36, 5, -12, 9, -21])
output:
[-21, -12, 5, 9, 36]

2. 
sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按**绝对值**大小排序：
input:
sorted([36, 5, -12, 9, -21], key=abs)
output:
[5, 9, -12, -21, 36]
其中key指定的函数作用于每一个元素上，再将返回值进行比较

3. 
一个字符串排序：
input:
sorted(['bob', 'about', 'Zoo', 'Credit'])
output:
['Credit', 'Zoo', 'about', 'bob']

如果要使该排序忽略大小写只需将key后的映射修改一下：
input:
sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower)
output:
['about', 'bob', 'Credit', 'Zoo']

4. 
要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True:
input:
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
output:
['Zoo', 'Credit', 'bob', 'about']

### 返回函数
1. 
将函数作为返回值：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
通过这样的方法，调用lazy_sum时返回的不是结果而是函数：
input:
f = lazy_sum(1, 3, 5, 7, 9)
f
output:
<function lazy_sum.<locals>.sum at 0x101c6ed90>
input:
f()
output:
25

2. 
这种在一个函数中又定义了另一个函数内，内层函数可以引用外部函数的参数和局部变量，返回时相关变量和参数都保存在返回函数中的结构成为“闭包”。

即使传入相同的参数，f1，f2结果互不影响：
input:
1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
f1==f2
output:
False

3. 闭包
一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。下面是一个例子：
input:
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

output:
f1()
9
f2()
9
f3()
9
全部都是9。原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

返回闭包时牢记的一点就是：返回函数**不要引用任何循环变量**，或者后续会发生变化的变量。

如果一定要引用循环变量就再创建一个函数，用该函数的参数绑定循环变量当前的值。

### 匿名函数
1. 
input:
list(map(lambda x : x * x , [1,5,6,8,9,7]))
output:
[1, 25, 36, 64, 81, 49]
用lambda表示匿名函数，冒号前的x表示函数参数，匿名函数**只能有一个表达式**，不用写return，返回值就是该表达式的结果。
可以看出，lambda x : x * x 就是：
def f(x):
    return x * x
也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
input:
f = lambda x: x * x
f(5)
output:
25

### 偏函数
1. 
利用偏函数可以固定函数的参数
int()函数原本默认将字符串转换成10进制，我们可以通过修改其参数的形式将字符串转换为其他进制:
input:
int('12345', base=8)
output:
5349

2. 
我们也可以通过定义一个新函数来解决这个问题：
input:
def int2(x, base = 2):
    return int(x, base)

int2('101101001')
output:
361

3. 
可以通过functools.partial来创建一个偏函数，不需要我们自己定义int2():
input:
import funtools
int2 = functools.partial(int, base = 2)
int2('10111110')
output:
190

4. 
创建偏函数时，可以接受*args ,**kw 这三个参数。上面的base = 2实际上将 **kw固定了，而下面的例子是将 *args中的一部分固定了：
input:
import functools
max10 = functools.partial(max, 10)
max10(2,6,8)
output:
10
当传入：
max10 = functools.partial(max, 10)
实际上会把10作为*args的一部分自动加到左边，相当于args = (10, 2, 6, 8)
max(*args)

这样可以使函数调用更加简单

## 模块
### 使用模块
1. 
在Python中，一个.py文件就称为一个模块。使用模块大大提高了程序的可维护性，可以避免函数名与变量名的冲突。

2. 
https://www.liaoxuefeng.com/files/attachments/001388366035986b515b38d149b4efaaac3f2c721813d2c000/0
如图所示，一个abc.py的文件就是一个名字叫abc的模块，一个xyz.py的文件就是一个名字叫xyz的模块。假设我们的abc和xyz这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。方法是选择一个顶层包名，比如mycompany，按照如图目录存放。

3. 
引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，abc.py模块的名字就变成mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz

4. 
每一个包目录下都必须有一个__init__.py文件，如果没有这个文件python就会将其当作普通目录而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany

5. 
类似的，可以有多级目录，组成多级层次的包结构。比如如下的目录结构：
https://www.liaoxuefeng.com/files/attachments/00138836605526535c9bebcbf414c3dae2430c50bbeef29000/0

6. 
自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。

## 面向对象编程
面向对象编程是一种程序设计思想，面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。
假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示：
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }
而处理学生成绩可以通过函数实现，比如打印学生的成绩：

def print_score(std):
    print('%s: %s' % (std['name'], std['score']))

如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象，这个对象拥有name和score这两个属性（Property）。如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，然后，给对象发一个print_score消息，让对象自己把自己的数据打印出来。
input:
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
output:
Bart Simpson: 59
Lisa Simpson: 87

### 类和实例
1. 定义类
面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
在Python中，定义类是通过class关键字。class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。

2. 创建实例
定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过**类名+()**实现的：
input:
class Student(object):
    pass

bart = Student()
bart
output:
<__main__.Student at 0x139aa74f048>

可以看到，变量bart指向的就是一个Student的实例，后面的0x139aa74f048是内存地址，每个object的地址都不一样，而Student本身则是一个类。

3. 绑定实例的属性
input:
bart.name = 'Bart Simpson'
bart.name
output:
'Bart Simpson'

由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

(注意：特殊方法"init"前后有两个下划线)

注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去。

4. 和普通函数区别
和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

5. 数据封装
我们可以通过外部函数来访问name和score这些数据：
def print_score(std):
    print('%s: %s' % (std.name, std.score))

但是，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

我们从外部看Student类，就只需要知道，创建实例需要给出name和score，而如何打印，都是在Student类的内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。

封装的另一个好处是可以给Student类增加新的方法，比如get_grade：
input:
class Student(object):
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'
bart.get_grade()
output:
'C'