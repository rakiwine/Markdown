#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/01/31
# file: 等待时间.py
# Email:
# Author: rakiwine
import collections
import re

_list = []

with open("../game-out.log", "r", buffering=-1, encoding="UTF-8") as f:
    for line in f:
        line = line.strip("\n")

        if "waitDurationInterval 277916576169066496" in line:
            _list.append(line)

# [32m[2023-01-31 14:16:14.705] [INFO] console - [39mwaitDurationInterval 275343192386174976 1155 0
pattern = re.compile(r"waitDurationInterval 277916576169066496 ([\d]{1,}) ([\d]{1,})")

# ret = pattern.search("console - [39mwaitDurationInterval 275343192386174976 1155 0")
# print(ret.groups())

_dict = {}
for index, line in enumerate(_list):
    ret = pattern.search(line)
    roomId = ret.groups()[0]
    time = ret.groups()[1]
    if _dict.get(roomId, None) is not None:
        _dict[roomId].append(time)
    else:
        _dict[roomId] = [time]

for key, value in _dict.items():
    print(key, value)