#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/20
# file: _2_String.py
# Email:
# Author: rakiwine


Str = "1234567890Ab"

# \r \t \n

count = 0
for item in dir(Str):
    if not item.startswith("_") and not item.startswith("__"):
        # print("Str.{}()".format(item))
        count += 1
# print(count)


# 字符串转移字符
def str_transferred_meaning():
    pass
    # \(在行尾时)	续行符
    # \\	反斜杠符号
    # \'	单引号
    # \"	双引号
    # \a	响铃
    # \b	退格(Backspace)
    # \e	转义
    # \000	空
    # \n	换行
    # \v	纵向制表符
    # \t	横向制表符
    # \r	回车
    # \f	换页
    # \oyy	八进制数，y 代表 0~7 的字符，例如：\012 代表换行。
    # \xyy	十六进制数，以 \x 开头，yy代表的字符，例如：\x0a代表换行
    # \other	其它的字符以普通格式输出


# 字符串操作符
def str_operation():
    pass
    # +       字符串连接
    # *       重复输出字符串
    # []	  通过索引获取字符串中字符
    # [:]	  截取字符串中的一部分
    # in	  成员运算符 - 如果字符串中包含给定的字符返回 True
    # not in  成员运算符 - 如果字符串中不包含给定的字符返回 True
    # r/R	  原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。
    # %	      格式字符串


# 新建空串
str0 = str()
str0 = ''

# 新建非空字符串
str0 = '非空字符串'
str0 = str(['任意类型'])       # "['任意类型']"
str0 = str(range(10))         # 'range(0, 10)'

# 增加元素
str0 = '原字符串'
str0 = str0[0] + '新字符串'
str0 = str0 + '新字符串'
str0 = str0 * 2

# 查询元素
str0.rfind('j', 1, 3)           # 指定范围 存在返回第一次位置  否则返回-1 不终止程序
str0.rindex('j', 1, 3)          # 指定范围 存在返回第一次位置  否则报错   终止程序


# 作用 创建字符映射的转换表 两个字符串一一对应 长度相同
# 返回 基于映射转换老串产生的新串
# 结果 不改变原字符串
trans = str.maketrans("012345678", "123456789")
"012345678".translate(trans)

# 作用 从左到右 以指定字符串分割 次数大于不报错
# 返回 列表
# 结果 不改变原字符串
str0.split('a', 1)
str0.rsplit("5", 5)
# 作用 按照行('\r', '\r\n', \n')分隔 keepends 用于保留换行符
# 返回
# 结果 不改变原字符串
str0.splitlines(keepends=True)
# Str.partition()       根据指定的分隔符将字符串进行分割。
# Str.rpartition()      右起

# 作用 根据指定的分隔符将字符串进行分割
# 返回 结果三元组 ("左", "分隔符", "右")
# 结果 不改变原字符串
str0.partition(" ")
str0.rpartition(" ")
'a'.join(["str", "str"])       # 将‘a’添加到【字符串元素】之间并且生成串  必须是字符串元素


# 字符串输出样式
def output_style_format():
    # 作用 用于将 str 类型转换成 bytes 类型 编码 GBK GB2312 UTF-8
    # 返回 bety类型的编码
    # 结果 不改变原字符串
    # 默认为 'strict',意为编码错误引起一个UnicodeError。
    # 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
    str0.encode("utf-8", "ignore")

    # 作用 指定次数替换指定字符串 次数大于不报错
    # 返回
    # 结果 不改变原字符串
    str0.replace('old', 'new', 2)
    # 作用 \t为4个空格长度的制表符 替换 \t 为 tabsize 个空格 默认tabsize=8
    # 返回
    # 结果 不改变原字符串
    str0.expandtabs(tabsize=8)

    # 样式调整
    str0.strip('字符串集合')   # 当左右一个都不符合时停止 默认为空格 table 回车
    str0.lstrip('字符串集合')  # 当左边一个都不符合时停止
    str0.rstrip('字符串集合')  # 当右边一个都不符合时停止
    del str0                 # 删除全部

    # 输出样式 不改变原字符串
    str0.center(100, '*')       # 居中填充*
    str0.ljust(100, '*')        # 左填充*
    str0.rjust(100, '*')        # 右填充*
    str0.zfill(100)             # 左填充0 str0.ljust(100, '0')

    # 作用 格式化输出字符串
    # 返回 格式化字符串
    # 结果 在不改变原字符串情况下 地址相同 否则 另起地址
    "format", Str.format(1), id(Str)
    "format", Str.format(1), id(Str.format(1))
    # 作用 格式化输出字符串 仅适用于字典
    # 返回 格式化字符串
    # 结果 在不改变原字符串情况下 地址相同 否则 另起地址
    Str.format_map({}), id(Str.format(1))
    "{name} 456".format(**{"name": 123})
    "{st[name]} 456".format(st={"name": 123})
    "{name} 456".format_map({"name": 123})

    # %控制		“%s%d%f%%”%(string,int,float)
    # F控制		F”{variable}{variable}”

    # 结果 不改变原字符串
    str0.swapcase()                # 大写《=互相转换=》小写
    str0.upper()                   # 字符串全部大写

    str0.lower()                   # 字符串全部小写
    str0.casefold()                # 与 lower()方法相似，但是casefold()方法更强大，更具攻击性

    str0.capitalize()              # 首字母大写
    str0.title()                   # 每个单词首字母大写


# 字符串查找
def sub_str_find():
    # 作用 指定范围 判断字符串末尾开始/结束
    # 返回 True False
    # 结果 不改变原字符串
    str0.startswith('abc', -100, -100)
    str0.endswith('ijk', -100, -100)

    # 作用 指定范围 查询子串的出现次数
    # 返回
    # 结果 不改变原字符串
    str0.count('a', -100, 100)

    # 作用 在指定区间 查找子串 第一次出现位置
    # 返回 成功索引 失败-1
    # 结果 不改变原字符串
    str0.find(".", -100, -100)
    # 作用 在指定区间 查找子串 最后一次出现位置
    # 返回 成功索引 失败-1
    # 结果 不改变原字符串
    str0.rfind(".", -100, -100)

    # 作用 在指定区间 查找子串 第一次出现位置
    # 返回 成功索引 失败异常
    # 结果 不改变原字符串
    str0.index("0", -100, 100)
    # 作用 在指定区间 查找子串 最后一次出现位置
    # 返回 成功索引 失败异常
    # 结果 不改变原字符串
    str0.rindex("0", -100, 100)


str0.isnumeric()               # is判断 数字字符 只针对unicode对象
str0.isdecimal()               # is判断 十进制字符 只针对unicode对象 u"123465"
str0.isprintable()             # is判断 打印为空 \n \t

str0.isspace()                 # is判断 全空格
str0.isascii()                 # is判断 空\ASCII
str0.isdigit()                 # is判断 全数字 0\正数
str0.isalnum()                 # is判断 字母\数字
str0.isalpha()                 # is判断 字母

str0.islower()                 # is判断 全小写
str0.isupper()                 # is判断 全大写
str0.istitle()                 # is判断 全单词首字母大写

str0.isidentifier()            # is判断 Python标识符\变量名是否合法

# 字符串切片
# 从正数第一个正着走
print(1, str0[::1])
print(2, str0[0:1000:1])
# 从倒数最后一个倒着走
print(3, str0[::-1])
print(4, str0[-1:-1000:-1])
# [start: end: sep] start + sep -> end 能够前进才存在值

