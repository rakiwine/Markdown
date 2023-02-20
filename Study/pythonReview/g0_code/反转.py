#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/24
# file: 反转.py
# Email:
# Author: rakiwine 

str_ = "123456789"
print("字符串 切片", str_[::-1])
# 可以使用海象运算符
print("字符串 for", "".join(str_[len(str_) - 1 - i] for i in range(len(str_))))
# reversed 返回一个反转的迭代器（元组、列表、字符串、range）
print("字符串 reversed", "".join(i for i in reversed(str_)))

list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("列表 切片", list_[::-1])
print("列表 for", [list_[len(list_) - 1 - i] for i in range(len(list_))])
print("列表 reversed", [i for i in reversed(list_)])
# 将原列表反转 无返回值
list_.reverse()
print("列表 reverse", list_)

tuple_ = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print("元组 切片", tuple_[::-1])
print("元组 for", tuple(tuple_[len(tuple_) - 1 - i] for i in range(len(tuple_))))
print("元组 reversed", tuple(i for i in reversed(tuple_)))

dict_ = {1: 2, 3: 4, 5: 6, 7: 8, 9: 0}
print(dict_)

print({k: dict_[k] for k in reversed(list(dict_.keys()))})
print({v: k for k, v in dict_.items()})
print(dict(zip(dict_.values(), dict_.keys())))
