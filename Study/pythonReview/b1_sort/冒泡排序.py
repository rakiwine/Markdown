#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/08/01
# file: 冒泡排序.py
# Email:
# Author: TSZ

# 第一轮排序，此时整个序列中的元素都位于待排序序列，依次扫描每对相邻的元素，并对顺序不正确的元素对交换位置


def mao_pao(num_list):
    num_len = len(num_list)
    # 控制循环的次数
    for j in range(num_len):
        # 添加标记位 用于优化(如果没有交换表示有序,结束循环)
        sign = False
        # 内循环每次将最大值放在最右边
        for i in range(num_len - 1 - j):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                sign = True

            # 如果没有交换说明列表已经有序，结束循环
            if not sign:
                break

if __name__ == '__main__':
    a = [1, 3, 4, 2, 6, 9, 12, 3, 22]
    mao_pao(a)
    print(a)
