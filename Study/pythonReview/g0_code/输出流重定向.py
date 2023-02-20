#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/30
# file: 输出流重定向.py
# Email:
# Author: TSZ

import sys


# 输出流重定向
class OutRedirection:
    """
    输出重定向
    """

    def __init__(self):
        self.buff = ''
        self.__console__ = sys.stdout

    def write(self, output_stream):
        self.buff += output_stream

    def to_console_and_file(self, file_path):
        sys.stdout = self.__console__
        print(self.buff)

        f = open(file_path, 'w')
        sys.stdout = f
        print(self.buff)
        f.close()

    def to_console(self):
        sys.stdout = self.__console__
        print(self.buff)

    def to_file(self, file_path):
        f = open(file_path, 'w')
        sys.stdout = f
        print(self.buff)
        f.close()

    def flush(self):
        self.buff = ''

    def reset(self):
        sys.stdout = self.__console__


obj = OutRedirection()
sys.stdout = obj

print("ces")

obj.write("test")

obj.to_console()
# obj.to_file("out_log.txt")
# obj.to_console_and_file("out_log.txt")
obj.flush()
obj.reset()