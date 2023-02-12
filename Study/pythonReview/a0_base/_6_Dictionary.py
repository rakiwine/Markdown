#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/21
# file: _6_Dictionary.py
# Email:
# Author: rakiwine

count = 0

for item in dir({}):
    if not item.startswith("_") and not item.startswith("__"):
        # print("_dict.{}()".format(item))
        count += 1
# print(count)

# 有序 dict 3.6及之后
# 无序 dict 3.6之前

# 初始化 列表导入
_dict = dict(name="maya", age=25, money="Zero")

for key, value in _dict.items():
    print(key, value)

# 初始化 依次设置
_dict = dict()
_dict["name"] = "maya"
_dict["age"] = 25
_dict["money"] = "Zero"

for key, value in _dict.items():
    print(key, value)

# 常用函数
# _dict.get()
# _dict.update()

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
print(list(_dict.values())[0])
# 适用于数据量多的时候会更快
print(next(iter(_dict.values())))

# 删除最后加入的
_dict.popitem()
# 删除第一个加入的
_iterDictKey = next(iter(_dict))
_dict.pop(_iterDictKey)
# 最后一个移到最前

# 最后一个移到最后
_dict[""] = _dict.pop("")















