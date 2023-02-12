#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/02/01
# file: 有序字典.py
# Email:
# Author: rakiwine

import collections

count = 0

for item in dir(collections.OrderedDict()):
    if not item.startswith("_") and not item.startswith("__"):
        # print("_dict.{}()".format(item))
        count += 1
# print(count)

# 初始化 列表导入
_dict = collections.OrderedDict(name="maya", age=25, money="Zero")

for key, value in _dict.items():
    print(key, value)

# 初始化 依次设置
_dict = collections.OrderedDict()
_dict["name"] = "maya"
_dict["age"] = 25
_dict["money"] = "Zero"

for key, value in _dict.items():
    print(key, value)

# 初始化 排序
dd = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

kd = collections.OrderedDict(sorted(dd.items(), key=lambda item: item[0]))
vd = collections.OrderedDict(sorted(dd.items(), key=lambda item: item[1]))

print(kd)
print(vd)

# 常用函数
# _dict.get()
# _dict.update()

# move_to_end(指定一个key，把对应的key-value移到最后)
_dict["name"] = "maya"
_dict["age"] = 25
_dict["money"] = "Zero"
_dict.move_to_end("name")  # 将name移到最后
_dict.move_to_end("name", last=False)  # 设置last为False, 将money移到最前面

# 对标
_dict.items()
_dict.keys()
_dict.values()

# fromkeys(指定一个列表，把列表中的值作为字典的key,生成一个字典)
name = ['tom', 'lucy', 'sam']
_dict.fromkeys(name)
_dict.fromkeys(name, 20)
# clear(清空有序字典)
_dict.clear()
# copy(拷贝)
new_dic = _dict.copy()
# pop(获取指定key的value，并在字典中删除)
_dict.pop("name")  # 删除name, 注意必须指定关键字key
# setdefault(获取指定key的value，如果key不存在，则创建)
val = _dict.setdefault('k5')
# 获取加入的第一个元素

# 删除最后加入的
_dict.popitem()
# 删除第一个加入的
_dict.popitem(last=False)
# 最后一个移到最前
_dict.move_to_end("", last=False)
# 最后一个移到最后
_dict.move_to_end("", last=True)












