#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/30
# file: 模拟交互python环境.py
# Email:
# Author: TSZ


# 模拟交互python逻辑
def interactive(code):
    try:
        result = eval(code)
        if result is not None:
            print(repr(result))
    except SyntaxError:
        exec(code)