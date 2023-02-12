#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/25
# file: 斐波那契数列.py
# Email:
# Author: rakiwine 

a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

import sys


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()