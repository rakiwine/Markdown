#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/24
# file: _with.py
# Email:
# Author: rakiwine 


# 打开关闭一个文件
# 释放一个锁
# 创建一个临时的代码补丁
# 在特殊环境下运行受保护的代码

# 任何实现了 _enter_(self) 和 _exit_(self,exc_type,exc_value,traceback) 方法的对象都可称之为上下文管理器，
# 上下文管理器对象可以使用 with 关键字。


class File(object):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("entering")
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, *args):
        print("will exit")
        self.f.close()


with File('out.txt', 'w') as f:
    print("writing")
    f.write('哈哈哈，你好啊！')
