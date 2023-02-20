#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/02/06
# file: test.py
# Email:
# Author: rakiwine


_list = []

count = 0
for item in dir(_list):
    if not item.startswith("_") and not item.startswith("__"):
        # print("_list.{}()".format(item))
        count += 1
# print(count)

# _list.append()
# _list.clear()
# _list.copy()
# _list.count()
# _list.extend()
# _list.index()
# _list.insert()
# _list.pop()
# _list.remove()
# _list.reverse()
#
l = [5, 3, 7, 8, 1]
sorted(l)
print(_list.sort())
