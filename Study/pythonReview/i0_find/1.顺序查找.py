#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/23
# file: 1.顺序查找.py
# Email:
# Author: rakiwine 

# 缺点：是当n很大时，平均查找长度较大，效率低；
# 优点：是对表中数据元素的存储没有要求。另外，对于线性链表，只能进行顺序查找。


def sequential_search(_lis, _key):
    for index, item in enumerate(_lis):
        if item == _key:
            return index
    else:
        return False


if __name__ == '__main__':
    lis = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    print(sequential_search(lis, 0))