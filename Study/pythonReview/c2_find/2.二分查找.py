#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/23
# file: 2.二分查找.py
# Email:
# Author: rakiwine


def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (right - left) // 2 + left

        num = nums[mid]

        if num == target:
            return mid
        elif num > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == '__main__':
    lis = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    print(search(lis, 5))