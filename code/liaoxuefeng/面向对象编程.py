# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
面向对象编程 : 数据封装、继承和多态
'''


'''
类和实例
'''
# 在类中定义的函数第一个参数永远是实例变量 self，且调用时不用传递该参数
class Student(object):
    def __init__(self, name, score):
        # self 参数表示创建的实例本身
        self.name = name
        self.score = score

# 创建实例通过类名+()实现
kyon = Student('Kyon Huang', 99)

# 可以自由地给一个实例变量绑定属性
kyon.gender = 'Male'



'''
访问限制
'''
# 如果要让内部属性不被外部访问，可以把属性名前加上两个下划线 __，将其变成私有变量
class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_person(self):
        print('%s: %s' % (self.__name, self.__age))

# 变量名类似 __xxx__ 的，是特殊变量，而非私有变量
# 变量名以一个下划线开头的，_xxx，外部可以访问，但一般视为私有变量

# Python 解释器对外把 __name 变量改成了 _Person__name
# 因此，不要在外部用 __name 访问



'''
继承和多态
'''
# 作为动态语言，Python 并不要求严格的继承体系



'''
获取对象信息
'''
# 判断基本数据类型
type(123) == type(456)    # True
type(123) == int    # True
type('abc') == type('123')    # True
type('abc') == str    # True
type('abc') == type(123)    # False

# types 模块 : 用其中定义的常量来判断函数类型
import types
def fn():
    pass

type(fn) == types.FunctionType    # True
type(abs) == types.BuiltinFunctionType    # True
type(lambda x: x) == types.LambdaType    # True
type((x for x in range(10))) == types.GeneratorType    # True

# 对于有继承关系的 class，使用 isinstance() 函数比 type() 更方便

# dir() : 获得一个对象的所有属性和方法
# 返回一个包含字符串的 list
dir('ABC')    # ['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']

# getattr(), setattr(), hasattr() : 获取、设置、检测是否有属性
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

hasattr(obj, 'x')   # True
obj.x    # 9
hasattr(obj, 'y')    # False
setattr(obj, 'y', 19)
hasattr(obj, 'y')    # True
getattr(obj, 'y')    # 19
obj.y    # 19

# 如果试图获取不存在的属性，会抛出 AttributeError 的错误
# 因此，可以给 getattr() 传入一个 default 参数，供属性不存在时返回
getattr(obj, 'z', 404)


# 示例 : 从文件流 fp 中读取图像
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None



'''
实例属性和类属性
'''
# 给实例绑定属性的方法是通过实例变量，或者通过 self 变量

# 类属性直接在 class 中定义
class Student(object):
    name = 'Student'

s = Student()
# 实例没有 name 属性，因此查找 class 的 name 属性
print(s.name)    # Student
print(Student.name)    # Student
s.name = 'Kyon'
print(s.name)    # Kyon
print(Student.name)    # Student
del s.name
print(s.name)    # Student
