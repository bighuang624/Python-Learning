# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
面向对象高级编程 : 多重继承、定制类、元类
'''


'''
使用 __slots__
'''
class Student(object):
    pass

s = Student()

# 动态语言的灵活性允许我们给实例绑定一个方法
def set_age(self, age):    # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)    # 给实例绑定一个方法
s.set_age(25)     # 调用实例方法
s.age    # 25


# 为了给所有实例都绑定方法，可以给 class 绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score
# 之后所有实例均可调用


# 如果想要限制实例的属性，例如，只允许对 Person 实例添加 name 和 age 属性
# Python 允许在定义 class 的时候，定义一个特殊的 __slot__ 变量，来限制该 class 实例能添加的属性
class Person(object):
    __slots__ = ('name', 'age')    # 用 tuple 定义允许绑定的属性名称

# 之后，为该 class 的实例绑定其他属性会报错
s.score = 99    # AttributeError: 'Person' object has no attribute 'score'

# __slots__ 定义的属性仅对当前类实例起作用，对继承的子类不起作用
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999
# 除非在子类中也定义 __slots__
# 这样，子类实例允许定义的属性就是自身的 __slots__ 加上父类的 __slots__


'''
使用 @property
'''






