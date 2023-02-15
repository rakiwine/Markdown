#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/02/13
# file: 查找对应行.py
# Email:
# Author: rakiwine

with open("../game-out.log", "r", buffering=-1, encoding="UTF-8") as f:
    for line in f:
        line = line.strip("\n")
        if "redisMonitor" in line:
            print(line)
