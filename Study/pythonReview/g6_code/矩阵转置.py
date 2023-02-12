#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/25
# file: 矩阵转置.py
# Email:
# Author: rakiwine 

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print([[row[i] for row in matrix] for i in range(4)])

list_ = []
for i in range(4):
    lis = []
    for row in matrix:
        lis.append(row[i])
    list_.append(lis)

print(list_)