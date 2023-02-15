#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/23
# file: base 文件.py
# Email:
# Author: rakiwine

# with open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None) as file:

# file:         必需，文件路径（相对或者绝对路径）。
# mode:         可选，文件打开模式
# buffering:    设置缓冲
# encoding:     一般使用utf8
# errors:       报错级别
# newline:      区分换行符
# closefd:      传入的file参数类型
# opener:       设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。


# 模式	描述
# t	    文本模式 (默认)。
# x	    写模式，新建一个文件，如果该文件已存在则会报错。
# b	    二进制模式。
# +	    打开一个文件进行更新(可读可写)。
# U	    通用换行模式（Python 3 不支持）。

# r	    以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。

# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。

# w	    打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。

# w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。

# a	    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。

# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。


# file.close()              关闭文件。关闭后文件不能再进行读写操作。
# file.flush()              刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
# file.fileno()             返回一个整型的文件描述符(filedescriptorFD整型), 可以用在如os模块的read方法等一些底层操作上。
# file.isatty()             如果文件连接到一个终端设备返回True，否则返回False。
# file.next()               Python3中的File对象不支持next()方法。返回文件下一行。

# file.read([size])                 从文件读取指定的字节数，如果未给定或为负则读取所有。文件大小 >2 倍内存则 error f.read()读到文件尾时返回""(空字串)。
# file.readline([size])             读取整行，包括"\n"字符。
# file.readlines([size int])         读取所有行并返回列表，若给定size int > 0，返回总和大约为size int字节的行, 实际读取值可能比size int较大, 因为需要填充缓冲区。

# 用来移动文件指针。
# 偏移量: 单位为字节，可正可负
# 起始位置: 0 - 文件头, 默认值; 1 - 当前位置; 2 - 文件尾
# f.seek(偏移量, [起始位置])

# 返回值 返回文件当前整数位置。
# file.tell()

# 从文件的首行首字符开始截断，截断文件为size个字符，无size表示从当前位置截断；截断之后后面的所有字符被删除，其中windows系统下的换行代表2个字符大小。
# 返回值
# file.truncate([size])

# 非字符串转换 字符串 写入文件
# 返回值 返回的是写入的字符长度。
# file.write(str)

# 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
# 返回值
# file.writelines(sequence)

# ASCII GB2312 Unicode UTF-8

# 通过迭代器访问。
# dict_ = {}
with open("os error dict.text", "r") as f:
    for line in f:
        # print(line)
        pass

# 读取整个文件,将整个文件的内容放在一个字符串变量中
# dict_ = {}
with open("os error dict.text", "r") as f:
    string = f.read()
    # print(string)

# 读取整行 每行包含\n
# dict_ = {}
with open("os error dict.text", "r") as f:
    while True:
        line = f.readline()
        if line:
            # print(type(line), line)
            pass
        else:
            break

# 一次性读取整个文件, 分割每行 每行包含\n
# dict_ = {}
with open("os error dict.text", "r") as f:
    string = f.readlines()
    # print(string)

# 文件存在 清空 不存在 创建
with open("path", "w") as f:
    pass