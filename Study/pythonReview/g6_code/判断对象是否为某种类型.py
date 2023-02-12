#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/28
# file: 判断对象是否为某种类型.py
# Email:
# Author: rakiwine 

# Python 3中有六个标准的数据类型 Numbers(数字)、String(字符串)、List(列表)、Tuple(元组)、Sets(集合)、Dictionaries(字典)
obj = ""

# type 不会认为子类是一种父类类型，不考虑继承关系
# isinstance 会认为子类是一种父类类型，考虑继承关系
print('isinstance', isinstance(count, int))
# X = type('X', (object,), dict(a=1)) 三个参数，返回新的类型对象
print('type', type(count))

# 判断对象是否为 int
print(" {}".format(isinstance(obj, int)))
print(" {}".format(isinstance(obj, float)))
print(" {}".format(isinstance(obj, complex)))

print(" {}".format(isinstance(obj, str)))
print(" {}".format(isinstance(obj, list)))
print(" {}".format(isinstance(obj, tuple)))
print(" {}".format(isinstance(obj, dict)))
print(" {}".format(isinstance(obj, set)))

print(" {}".format(isinstance(obj, type)))
print(" {}".format(type(obj) == int))

# 判断对象是否为函数
print(" {}".format(hasattr(obj, "__call__")))
print(" {}".format(callable(obj)))

# 判断对象是否为类
print(" {}".format(type(obj).__name__ == 'classobj'))
