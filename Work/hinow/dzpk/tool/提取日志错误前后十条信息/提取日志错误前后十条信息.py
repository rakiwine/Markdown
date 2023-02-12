#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/01/09
# file: 提取日志错误前后十条信息.py
# Email:
# Author: rakiwine

# 通过迭代器访问。
# _dict = {}



_list = []

with open("../game-out.log", "r", buffering=-1, encoding="UTF-8") as f:
    _lines = []
    _flag = True
    add_lines = 0

    for line in f:
        line = line.strip("\n")
        _lines.append(line)
        if "ERROR" in line and "JSON at position" not in line:
            # print(line)
            _flag = False
            add_lines = 10

        if len(_lines) == 10 and _flag and not add_lines:
            _lines.pop(0)

        if not add_lines:
            if not _flag:
                _flag = True
                _list.append(_lines)
                _lines = []
        else:
            add_lines -= 1

print(len(_list))

for i, j in enumerate(_list):
    print()
    print(i)
    for k in j:
        print(k)

# for i in _list[0]:
#     print(i)