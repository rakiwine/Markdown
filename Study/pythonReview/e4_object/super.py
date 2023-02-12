#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/27
# file: super.py
# Email:
# Author: TSZ

# 子类不调用 super 可以调用父类的方法 不能调用属性
# super()后，可以正常的调用父类的所有属性


class A:
    def __init__(self):
        print("A类中的属性")


class B:
    def __init__(self):
        print("B类中的属性")


class C(A, B):
    def __init__(self):
        print("C类中的属性")
        super(B, self).__init__()



c = C()