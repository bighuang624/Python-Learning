# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
函数式编程 : 抽象程度很高的编程范式
特点 : 允许把函数本身作为参数传入另一个函数，还允许返回一个函数
纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的
由于 Python 允许使用变量，因此，Python 不是纯函数式编程语言
'''


'''
高阶函数 : 一个函数可以接收另一个函数作为参数
'''
def add(x, y, f):
    return f(x) + f(y)

add(-5, 6, abs)

'''
map(func, Iterable) : 将传入的函数依次作用到序列的每个元素
return Iterator
'''
list(map(lambda x: x * x, [1, 2, 3, 4, 5]))    # [1, 4, 9, 16, 25]

'''
reduce(func, Iterable) : 把结果继续和序列的下一个元素做累积计算
注意需要 from functools import reduce 来导入 reduce
'''
from functools import reduce
reduce(lambda x, y: 10 * x + y, [1, 3, 5, 7, 9])    # 13579

'''
filter(func, Iterable) : 过滤序列
return Iterator
'''
def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))    # ['A', 'B', 'C']

'''
sorted(Iterable, key=func, reverse=False) : 根据 key 函数实现自定义排序，reverse 为 True 时反向排序
'''
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)    # ['Zoo', 'Credit', 'bob', 'about']



'''
返回函数
'''
# 调用作为返回值的函数时才真正计算
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
f    # <function lazy_sum.<locals>.sum at 0x101c6ed90>
f()    # 25

# 在函数 a 中又定义了函数 b，内部函数可以引用外部函数的参数和局部变量
# 函数作为返回值时，相关参数和变量都保存在返回的函数。这种程序结构称为“闭包”

# 因为返回的函数并非立即执行，因此返回闭包时，返回函数不要引用任何循环变量，或者后续会发生变化的变量!
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()    # 所引用的变量 i 都变成了 3
f1()    # 9
f2()    # 9
f3()    # 9

# 练习 : 利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')



'''
匿名函数 lambda
限制 : 只能有一个表达式
'''
# 把匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x : x * x
f    # <function <lambda> at 0x101c6ef28>
f(5)    # 25

# 把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y



'''
装饰器 decorator : 在代码运行期间动态增加功能
'''
# 定义一个能打印日志的 decorator
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 把 @log 放到 now() 函数的定义处，相当于执行语句 now = log(now)
@log
def now():
    print('2018-8-8')

# 调用 now() 将执行 log() 函数中返回的 wrapper() 函数
now()    
# call now():
# 2018-8-8


# 如果 decorator 本身需要传入参数，那就需要编写一个返回 decorator 的高阶函数
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 相当于 now = log('execute')(now)
@log('execute')
def now():
    print('2018-8-8')

now()
# execute now():
# 2018-8-8


# 按照上述写法有
now.__name__    # 'wrapper'
# 有些依赖函数签名的代码执行会出错
# functools.wraps : 将原始函数的 __name__ 等属性复制到 wrapper() 中
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)    # 在定义 wrapper() 的前面加上
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator



# 练习 : 设计一个 decorator，它可作用于任何函数上，并打印该函数的执行时间
import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        fn(*args, **kw)
        print('%s executed in %s ms' % (fn.__name__, time.time() - start))
        return fn
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


'''
偏函数 : 通过设定参数的默认值，降低函数调用的难度
'''
# functools.partial : 为一个函数的某些参数设置默认值，返回一个新的函数
import functools
int2 = functools.partial(int, base=2)
int('1000000')    # 64

# 创建偏函数时，实际可以接收函数对象、*args 和 **kw 三个参数
int2 = functools.partial(int, base=2)
int2('10010')
# 相当于
kw = { 'base': 2 }
int('10010', **kw)

max2 = functools.partial(max, 10)
max2(5, 6, 7)
# 会将 10 作为 *args 的一部分自动加到左边，相当于
args = (10, 5, 6, 7)
max(*args)
