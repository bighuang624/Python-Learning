# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
高级特性
切片、迭代、列表生成式、生成器、迭代器
'''


'''
切片
'''
L = list(range(100))
# 取前 10 个数
L[:10]
# 取后 10 个数
L[-10:]
# 前 11-20 个数
L[10:20]
# 前 10 个数，每两个取一个
L[:10:2]
# 所有数，每五个取一个
L[::5]
# 原样复制一个 list
L[:]



'''
迭代
'''
# 迭代 dict
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:    # 迭代 key
    print(key)
for value in d.values():    # 迭代 value
    print(value)
for k, v in d.items():    # 同时迭代 key 和 value
    print(key, value)

# collections 模块 Iterable 类型 : 判断一个对象是否是可迭代对象
from collections import Iterable
isinstance('abc', Iterable)    # True

# enumerate 函数 : 将 list 变为索引-元素对，实现下标循环
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)



'''
列表生成式
'''
[x * x for x in range(1, 11) if x % 2 == 0]    # [4, 16, 36, 64, 100]



'''
生成器 generator : 在循环的过程中不断推算出后续的元素
创建方法: 
    1. 把列表生成式的 [] 改为 ()
    2. 在函数定义中包含 yield 关键字
'''
# 用第一种方法创建生成器
g = (x * x for x in range(10))
# next() : 获得 generator 的下一个返回值
next(g)    # 0
next(g)    # 1
# 调用 next(g) 没有更多的元素时，抛出 StopIteration 的错误
# 因此，使用 for 循环更好
for n in g:
    print(n)

# 用第二种方法创建生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'

f = fib(6)
f    # <generator object fib at 0x104feaaa0>
# 在每次调用 next() 的时候执行，遇到 yield 语句返回，再次执行时从上次返回的 yield 语句处继续执行



'''
可迭代对象 Iterable : 可以直接作用于 for 循环的对象
迭代器 Iterator : 可以被 next() 函数调用并不断返回下一个值的对象

Iterator 表示一个数据流，不能提前知道长度
另外，其计算是惰性的，只有在需要返回下一个数据时它才会计算
'''
# 使用 isinstance() 判断一个对象是否是 Iterator 对象
from collections import Iterator
isinstance((x for x in range(10)), Iterator)    # True
isinstance([], Iterator)    # False

# iter() : 把 Iterable 变成 Iterator
isinstance(iter([]), Iterator)    # True

