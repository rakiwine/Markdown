#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/22
# file: 推导式.py
# Email:
# Author: rakiwine 


# 列表(list)推导式   []
list_ = [i for i in range(10)]
print(type(list_), list_)

# 字典(dict)推导式   {}
dict_ = {i: i for i in range(10)}
print(type(dict_), dict_)

# 集合(set)         {}
set_ = {i for i in range(10)}
print(type(set_), set_)

# 生成器对象
generator_ = (i for i in range(10))
print(type(generator_), generator_)

