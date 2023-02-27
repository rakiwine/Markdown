#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/21
# file: _6_Dictionary.py
# Email:
# Author: rakiwine

_dict = {}

count = 0
for item in dir(_dict):
    if not item.startswith("_") and not item.startswith("__"):
        print("_dict.{}()".format(item))
        count += 1
# print(count)

# 有序 dict 3.6及之后
# 无序 dict 3.6之前

# 字典key为不可变元素 数字 字母 元祖 字符串
# 新建空字典
_dict = {}
_dict = dict()

# 新建非空字典
_dict = {'key': 'value', ('name', 'age'): ('name', 20)}
_dict = dict(zip([1, 2, 3], ['a', 'b', 'c']))         # 将zip对象转换为字典对象
_dict = dict(key='value', tup=('name', 20))
_dict = dict.fromkeys([1, 2, 3], '初始值')             # value为初始值 不声明默认为None

# 获取字典key对应的value 键值对不存在 默认返None
_dict.get("", None)

# 用另一个字典更新当前字典 相同key覆盖value
_dict.update({})

print(1 in _dict)                # 查询key是否存在    字典key对象
print(1 in _dict.keys())         # 查询key是否存在    字典key对象
print(1 in _dict.values())       # 查询value是否存在  字典value对象
print(('key', 'value') in _dict.items())        # 查询(key,value)是否存在  字典item对象

del _dict["key"]

# 遍历
for item in _dict.items():
    # 元组
    print(item)
for k, v in _dict.items():
    print(k, v)

# for k in _dict:
for k in _dict.keys():
    print(k, _dict[k])

for v in _dict.values():
    print(v)

# 字典推导式
# { key_expr: value_expr for value in collection if condition }

# 常用函数

# 对标
_dict.items()
_dict.keys()
_dict.values()

# fromkeys(指定一个列表，把列表中的值作为字典的key,生成一个字典)
name = ['tom', 'lucy', 'sam']
_dict.fromkeys(name)
_dict.fromkeys(name, 20)

# clear(清空有序字典) del _dict 完全删除
_dict.clear()

# copy(拷贝)
new_dic = _dict.copy()

# pop(获取指定key的value，并在字典中删除) key不存在报错
_dict.pop("name")
# 存在返回value 不存在返回默认值
_dict.pop("name", "默认值")

# setdefault(获取指定key的value，如果key不存在，则创建)
val = _dict.setdefault("key", "value")

# 获取加入的第一个元素
print(list(_dict.values())[0])
# 适用于数据量多的时候会更快
print(next(iter(_dict.values())))

# 删除最后加入的 字典为空报错
_dict.popitem()

# 删除第一个加入的
_iterDictKey = next(iter(_dict))
_dict.pop(_iterDictKey, "默认值")

# 最后一个移到最前

# 最后一个移到最后
_dict[""] = _dict.pop("")















