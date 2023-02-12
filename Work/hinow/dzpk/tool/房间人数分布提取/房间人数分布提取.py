#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/01/31
# file: 房间人数分布提取.py
# Email:
# Author: rakiwine
import collections
import re

_list = []

with open("../game-out.log", "r", buffering=-1, encoding="UTF-8") as f:
    for line in f:
        line = line.strip("\n")

        if "game room分布" in line:
            _list.append(line)

pattern = re.compile(r"\[([ \d\,]*)\]")

# ret = pattern.search("[ 5,5]")
# print(ret.groups())

roomMinPeopleStart = 5
for index, line in enumerate(_list):
    ret = pattern.search(line)
    roomMap = ret.groups()[0].replace(" ", "")
    roomList = roomMap.split(",")

    count = 0
    _dict = {
        6: 0,
    }
    for room in roomList:
        room = int(room)
        count += room
        if _dict.get(room, None) is not None:
            _dict[room] += 1
        else:
            _dict[room] = 1

    # _tuple = [(key, value) for key, value in _dict.items()]
    # _dict = collections.OrderedDict(_tuple)

    # if count >= 108:
    #     print("{}\t{}\t{}\t{}\t{}\t{}".format(
    #         _dict.get("9", 0),
    #         _dict.get("8", 0),
    #         _dict.get("7", 0),
    #         _dict.get("6", 0),
    #         _dict.get("5", 0),
    #         str(_dict.get("4", 0)) + str(_dict.get("3", 0)) + str(_dict.get("2", 0)) + str(_dict.get("1", 0)))
    #         # max(_dict.get("4", 0), _dict.get("3", 0), _dict.get("2", 0), _dict.get("1", 0))
    #         # _dict.get("4", 0) + _dict.get("3", 0) + _dict.get("2", 0) + _dict.get("1", 0))
    #     )

    if _dict.get(roomMinPeopleStart + 1, 0) + 1 > _dict.get(roomMinPeopleStart, 0) and _dict.get(roomMinPeopleStart, 0) != 0:
        roomMinPeopleStart = roomMinPeopleStart + 1

    print(roomMinPeopleStart, count, _dict, min(_dict.keys()), _dict[min(_dict.keys())])
    # print(_dict, index, count, roomMinPeopleStart)
