#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/23
# file: 3.插值查找.py
# Email:
# Author: rakiwine 


def search(lis, key):
    low = 0
    high = len(lis) - 1

    while low <= high:
        # 计算mid值是插值算法的核心代码
        mid = low + int((high - low) * (key - lis[low]) / (lis[high] - lis[low]))
        print("low={}, mid={}, high={}" % (mid, low, high))
        print("mid=%s, low=%s, high=%s" % (mid, low, high))
        if key < lis[mid]:
            high = mid - 1
        elif key > lis[mid]:
            low = mid + 1
        else:
            return mid
    return False


if __name__ == '__main__':
    LIST = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = search(LIST, 5)
    print(result)