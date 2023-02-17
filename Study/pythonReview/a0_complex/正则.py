#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/23
# file: 正则.py
# Email:
# Author: rakiwine 

import re

str1 = 'hello world:luobo dazahui'

count = 0
for item in dir(re):
    if not item.startswith("_") and not item.startswith("__"):
        # print("re.{}()".format(item))
        count += 1
# print(count)

# re.A()
# re.ASCII()
# re.DEBUG()
# re.DOTALL()
# re.I()
# re.IGNORECASE()
# re.L()
# re.LOCALE()
# re.M()
# re.MULTILINE()
# re.Match()
# re.Pattern()
# re.RegexFlag()
# re.S()
# re.Scanner()
# re.T()
# re.TEMPLATE()
# re.U()
# re.UNICODE()
# re.VERBOSE()
# re.X()
#
# re.copyreg()
# re.enum()
# re.error()
# re.escape()

# re.fullmatch()
# re.functools()
# re.purge()

# re.sre_compile()
# re.sre_parse()
# re.subn()
# re.template()

# \A  指定字符：如果指定的字符位于字符串的开头，则返回匹配项。
# \b  指定开头结尾：返回指定字符位于单词开头或结尾的匹配项 （开头的“r”确保字符串被视为原始字符串）。
# \B  匹配中间字符：返回存在指定字符但不在单词开头（或结尾）的匹配项 （开头的“r”确保字符串被视为“原始字符串”）
# \d  匹配数字：返回字符串包含数字（0-9 之间的数字）的
# \D  匹配非数字：返回字符串不包含数字的匹配项
# \s  空格匹配：返回一个匹配字符串包含空白空间字符的匹配项。
# \S  匹配非空格：返回字符串不包含空格字符的匹配项
# \w  匹配任意数字和字母：返回一个匹配，其中字符串包含任何单词字符（从 a 到 Z 的字符，从 0 到 9 的数字，以及下划线 _ 字符）
# \W  匹配任意非数字和字母：返回字符串不包含任何单词字符的匹配项，在每个非单词字符中返回匹配（不在A和Z之间的字符。“！”，“？”空白位等）
# \Z  匹配结尾：如果指定的字符位于字符串的末尾，则返回匹配项。


# re.I(re.IGNORECASE) ：使匹配对大小写不敏感
# re.L(re.LOCAL) ：表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
# re.M(re.MULTILINE) ：多行匹配，影响 ^ 和 $
# re.S(re.DOTALL) ：使 . 匹配包括换行在内的所有字符
# re.U(re.UNICODE)：表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
# re.X(re.VERBOSE)：为了增加可读性，忽略空格和 # 后面的注释

# 加快速度，并重复使用
# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
pattern = re.compile(r"[\w]{4,20}@(.*)\.com$", re.I | re.M)

pattern.match("", 0, -1)
pattern.search("", 0, -1)
pattern.findall("", 0, -1)


# 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match() 就返回 none。
ret = re.match(r"([\w]{4,20})@(.*)\.com$", " rakiwine@163.com", re.I)
if ret is not None:
    # 返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
    print(ret.groups())
    print((ret.group(1), ret.group(2), ...))
    print(ret.span())
    print((ret.start(), ret.end()))

    # 0是本身匹配字符串 1是第一个组
    print(ret.group())
    print(ret.group(0))
    print(ret.group(1))
else:
    print("None")

# 扫描整个字符串并返回第一个成功的匹配。
ret = re.search(r"([\w]{4,20})@(.*)\.com$", " rakiwine@163.com", re.I)
if ret is not None:
    # 返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
    print(ret)
    print(ret.groups())
    print((ret.group(1), ret.group(2), ...))
    print(ret.span(), (ret.start(), ret.end()))

    # 0是本身匹配字符串 1是第一个组
    print(ret.group(), ret.group(0))
    print(ret.group(1), ret.group(2))
else:
    print("None")

# 替换字符串中的匹配项。
# count=0 表示替换所有的匹配
print(re.sub(r"\d+", "20", "123456", count=0, flags=re.I))


def double(matched):
    if matched is not None:
        value = int(matched.group('value'))
        return str(value * 2)
    else:
        return ""


print(re.sub(r"(?P<value>\d+)", double, "123456", count=0, flags=re.I))


# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，
# 如果有多个匹配模式，则返回元组列表，如果没有找到匹配的，则返回空列表。
# 存在分组 返回组 否则返回匹配
pattern = re.compile(r'(\w+)=(\d+)', re.I | re.M)
ret = re.findall(r"\d+", " rakiwine@163.com", re.I)
ret = pattern.findall(" set width=20 and height=10", -100, 100)

if ret is not None:
    print([])
    print(ret)
else:
    print("None")


# 找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
# 迭代之后为空
pattern = re.compile(r'(\w+)=(\d+)', re.I | re.M)
ret = re.finditer(r"\d+", " rakiwine@163.com", re.I)
ret = pattern.finditer(" set width=20 and height=10", -100, 100)

if ret is not None:
    print("finditer", [])
    # print("finditer", [i for i in ret])
    # print("finditer", [i.span() for i in ret])
    # print("finditer", [i.group() for i in ret])
    print("finditer", [i.groups() for i in ret])
else:
    print("None")

# 按照能够匹配的子串将字符串分割后返回列表
print(re.split(r":", "12345:6:7:89", 2, re.I))
print(re.split(r'\W+', 'runoob, runoob, runoob.'))
print(re.split(r'(\W+)', ' runoob, runoob, runoob.'))
