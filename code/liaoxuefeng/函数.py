# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
函数
'''


# help(func) : 在交互式函数查看指定 func 函数的帮助信息

'''
数据类型转换
'''
int('123')    # 123
int(12.34)    # 12
float('12.34')    # 12.34
str(1.23)    # '1.23'
bool(1)    # True
bool('')    # False



'''
定义函数
'''
# pass : 为空函数作占位符
def nop():
    pass


# 参数检查 : Python 解释器可以自动检查出函数个数不对，但是无法检查参数类型不对
# 因此，建议在函数内部用 isinstance() 进行数据类型检查
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 返回多个值 : 可以返回多个值，但实际上是返回单一的一个 tuple
# 可以多个变量同时接收一个 tuple，按位置赋给对应的值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)    # 151.96152422706632 70.0



'''
函数的参数
必选参数、默认参数、可变参数、关键字参数、命名关键字参数
'''
# 默认参数 : 必须指向不变对象
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
# 有多个默认参数时，调用可以按顺序提供默认参数，也可以把参数名写上以不按顺序提供部分默认参数


# *args 可变参数 : 函数声明时参数前加一个 *
# 允许传入 0 个或任意个参数，在调用时自动组装为一个 tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1, 2)    # 5
calc()    # 0
# 如果已经有一个 list 或者 tuple，要调用一个可变参数
# Python 允许在 list 或 tuple 前加一个 * 号，将其变为可变函数传入
nums = [1, 2, 3]
calc(*nums)    # 14


# **kw 关键字参数 : 函数声明时参数前加一个 **
# 允许传入 0 个或任意个含参数名的参数，在调用时自动组装为一个 dict
def student(name, age, **kw):
    print('name: ', name, 'age: ', age, 'other: ', kw)

person('Adam', 22, gender='M', major='Engineer')    # name: Adam age: 45 other: {'gender': 'M', 'major': 'Engineer'}
# 与可变参数类似，可以在 dict 前加一个 **，将其转换为关键字参数传入
extra = {'city': 'Beijing', 'major': 'Engineer'}
person('Jack', 24, **extra)


# 命名关键字参数 : 限制关键字参数的名字
# 命名关键字参数需要一个特殊分隔符 *，* 后面的参数被视为命名关键字参数
def teacher(name, age, *, city, gender):
    print(name, age, city, gender)

teacher('Jack', 34, city='Beijing', gender='M')    # Jack 34 Beijing M
# 如果函数定义中已有一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符 *
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
# 命名关键字必须传入参数名，否则调用将报错
# 如果缺少 *，Python 解释器将无法识别位置参数和命名关键字参数



# 参数组合 : 
# 在 Python 中定义函数，可以用必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# 但是参数定义的顺序必须如上
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
