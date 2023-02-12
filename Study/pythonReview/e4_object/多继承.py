#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/27
# file: 多继承.py
# Email:
# Author: rakiwine 

# python 继承多态

# python 继承多态

class Z:
    def __init__(self):
        print("Z")
        print("Z -- end")

class A:
    def __init__(self):
        print("A")
        print("A -- end")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()
        print("B -- end")

class C(A):
    def __init__(self):
        print("C")
        super().__init__()
        print("C -- end")

class D(B,C):
    def __init__(self):
        print("D")
        super().__init__()
        print("D -- end")

if __name__ == '__main__':
    d = D()

# 同一个超类 A B(A) C(A) D(B,C)
# D B C A C B D
# 同取一超类

# 不同超类 Z A B(Z) C(A) D(B,C)
# D B Z B D
# 不同少后超类

# 多继承 -> 广度优先搜索
# 单继承 -> 深度优先搜索

# 多继承计算
# https://blog.csdn.net/weixin_39576336/article/details/110776760