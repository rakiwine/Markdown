#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/21
# file: _7_str_list_tuple.py
# Email:
# Author: rakiwine


str_list_tuple = []

# 列表切片
# 从正数第一个正着走
print(str_list_tuple[::-1])
print(str_list_tuple[0:1000:1])
# 从倒数最后一个倒着走
print(str_list_tuple[:])
print(str_list_tuple[-1:-1000:-1])
# [start: end: sep] start + sep -> end 能够前进才存在值

# 遍历
for i in str_list_tuple:
    pass

for i in range(len(str_list_tuple)):
    pass

for i, v in enumerate(str_list_tuple):
    pass


# 查询
print(1 in "")
print(1 in [])
print(1 in ())

# 作用 统计在字符串/列表/元组中某个字符出现的次数
# 返回 字符在区间范围内出现次数
# 结果 不改变原型
print("".count("0", -100, 100))
print(["0", "0", ].count("0"))
print(("0", ).count("0"))

# 作用 在指定区间 查找子串 第一次出现位置
# 返回 成功索引 失败异常
# 结果 不改变原字符串
print("0".index("0", -100, 50))
print(["0"].index("0", -100, 50))
print(("0", ).index("0", -100, 50))
