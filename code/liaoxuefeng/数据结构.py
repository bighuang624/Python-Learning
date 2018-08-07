# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
数据结构：list, tuple, dict, set
'''


# list : 列表，是可以随时添加和删除元素的有序集合，元素类型可不同
classmates = ['Andy', 'Bob', 'Carlos']
classmates[1]    # 'Bob'
classmates[-1]    # 'Carlos'

# len(list) : 可以获得 list 元素的个数
len(classmates)    # 3

# append(item) : 往 list 中追加元素到末尾
classmates.append('Dean')

# insert(index, item) : 把元素插入到指定位置
classmates.insert(1, 'Mario')

# pop() : 删除 list 末尾的元素
classmates.pop()    # 'Dean'

# pop(index) : 删除指定位置的元素
classmates.pop(1)    # 'Mario'



# tuple : 元组，和 list 类似，但一旦初始化就不能修改，只能访问
# 因为 tuple 不可变，所以代码更安全
# 定义时必须确定 tuple 的元素
t = (1, 2)

# 定义只有一个元素的 tuple，必须加一个逗号,，来与小括号做区别
t = (1,)



# dict : 字典，可以理解为其他语言的 Map，使用 key-value 存储
d = {'Andy': 95, 'Bob': 80, 'Carlos': 85}
d['Andy']    # 95

# 通过直接赋值就可以实现增加 key 和覆盖 key 对应的 value
d['Kyon'] = 98

# 通过不存在的 key 访问会报错，有两种方法避免：
# 1. 通过 in 判断 key 是否存在
'Jay' in d    # False
# 2. 通过 get() 函数，如果 key 不存在，可以返回 None 或者自己指定的 value
d.get('Jay', -1)    # -1

# pop(key) : 删除一个 key 和对应的 value
d.pop('Bob')



# set : 集合，只存储 key 且无重复
# set() : 创建一个 set，需要提供一个 list 作为输入
s = set([1, 2, 3])

# add(key) : 添加元素到 set 中，重复添加无效果
s.add(4)

# remove(key) : 删除元素
s.remove(4)

# 两个 set 可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2    # {2, 3}
s1 | s2    # {1, 2, 3, 4}



