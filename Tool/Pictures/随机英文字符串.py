#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/01/09
# file: 随机英文字符串.py
# Email:
# Author: rakiwine

import random


# chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
print('chr', chr(65))
# 将一个字符作为参数，返回对应的 ASCII 数值转换为它的整数值 Unicode 字符超出了 Python 定义范围 引发一个 TypeError 的异常
print('ord', ord("a"))

_list = [chr(random.randint(97, 122)) for i in range(26)]
print("".join(_list))