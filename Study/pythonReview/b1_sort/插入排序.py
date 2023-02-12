#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/08/01
# file: 插入排序.py
# Email:
# Author: TSZ


def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key