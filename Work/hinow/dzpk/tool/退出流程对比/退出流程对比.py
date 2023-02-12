#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/02/07
# file: 退出流程对比.py
# Email:
# Author: rakiwine

import re

rpcQuitGamePushList = []
GameEnterList = []
GameQuitList = []
RoomEnterList = []
RoomQuitList = []
RoomTakeList = []
RoomStandList = []

with open("../game-out.log", "r", buffering=-1, encoding="UTF-8") as f:
    for line in f:
        line = line.strip("\n")

        # if "rpcQuitGamePush" in line:
        #     rpcQuitGamePushList.append(line)

        # if "userGameEnter" in line:
        #     GameEnterList.append(line)

        # if "userGameQuit" in line:
        #     GameQuitList.append(line)

        # if "userRoomEnter" in line:
        #     RoomEnterList.append(line)

        # if "userRoomQuit" in line:
        #     RoomQuitList.append(line)

        # if "userRoomTake" in line:
        #     RoomTakeList.append(line)

        if "standAndExitDebug" in line:

            if "userRoomStand" in line:
                print(line)

            if "userRoomQuit" in line:
                print(line)

            if "userGameQuit" in line:
                print(line)

        if "game room人数" in line:
            print(line)

# 102 46
# print(len(RoomTakeList))
# print(len(RoomStandList))
# print(len(RoomEnterList))
# print(len(RoomQuitList))
# print(len(GameEnterList))
# print(len(GameQuitList))
# print(len(rpcQuitGamePushList))