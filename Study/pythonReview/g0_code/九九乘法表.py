#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/23
# file: 九九乘法表.py
# Email:
# Author: rakiwine

for index_i in range(1, 10):
    for index_j in range(1, index_i + 1):
        print("{}*{}={}".format(index_i, index_j, index_i * index_j), end=" ")

    print()
