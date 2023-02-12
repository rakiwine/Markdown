#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/21
# file: _7_str_list_tuple.py
# Email:
# Author: rakiwine 

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
