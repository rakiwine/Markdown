#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/01/30
# file: globals locals.py
# Email:
# Author: rakiwine

# 如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。
# 如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。
# 两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。

# 预先定义 防止遍历时 字典大小改变报错
key = None
ces = None

for key, ces in locals().items():
    print(key, ces)

print()
print(locals()["key"])
print(locals()["ces"])
print()

for key, ces in globals().items():
    print(key, ces)
