#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/21
# file: _0_base.py
# Email:
# Author: rakiwine 

import keyword
print(keyword.kwlist)
"""
[
    'import', 'as', 'from',
    'class', 'def',
    'global',
    'False', 'None', 'True',
    'break', 'continue', 'return',
    'if', 'elif', 'else',
    'for',
    'try', 'except', 'finally', 'pass', 'raise',
    'is', 'and', 'in', 'not', 'or',
    'with',  'while', 'del', 'lambda',
    'assert', 'async', 'await', 
    'nonlocal',  'yield']
"""

# 弱类型语言不用定义变量的类型
param = 1

# 变量命名 [字母数字下划线] [字母下划线开头]
param_1 = 1
_param_1 = 1
# ①　小写单词_小写单词[_小写单词] test_one
# ②　小写单词首字母大写[首字母大写] testOne
# ③　首字母大写首字母大写[首字母大写] TestOne


# 数据类型分为 数字型 非数字型
# 数字型
_int = int()			# 转换为整型
_float = float()        # 转换为浮点型
_boolean = bool()
# 非数字型
_str = str()		   # 转换为字符串
_list = list()
_tuple = tuple()
_dict = dict()

# 输入输出
# 输出结果到控制台
print()
# 获取键盘输入 回车结束
input()


# 用来计算在字符串中的有效Python表达式,并返回一个对象
print(eval("True"))
print("测试")


# 可迭代对象
# list、tuple、dict、str generator生成器带yield 的generator function


# 有序 dict 3.7之后 str list tuple
# 无序 dict 3.6之前 set


# 不可变数据类型       整形int，浮点型，复数，布尔，固定集合 ，字符串 ，元组
# 可变数据类型         列表，字典，集合
# 不可变数据类型       是指变量的值发生改变时，其对应的内存地址也发生改变。
# 可变数据类型         是指变量的值发生改变时，其对应的内存地址不发生改变


# str()主要用来为终端用户输出一些信息，而repr()主要用来调试
# 如果都没有重写，那么就使用继承自Object这个父类的内容；
# 如果只有__repr__重写了，那么str()和repr()都是调用__repr__；
# 如果只有__str__重写了，那么str()和repr()各用各的；
# 如果两个都重写了，那么还是各用各的。
# str  看 子级str 子级repr 父级str
# repr 看 子级repr 父级str

