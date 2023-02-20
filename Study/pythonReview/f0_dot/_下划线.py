#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/24
# file: _下划线.py
# Email:
# Author: rakiwine

# _         单划线变量
#           它占了参数的位置却无法被调用，适用于必须要输出或输入的无用参数
_, lis = [], []

# _xx       约定成员私有
#           是程序员约定的指定私有变量和方法，指定的成员、属性只在类内可用，（其实可以被调用）
#           但在引入类的时候，如 from module import * 时，本来所有子函数都该被调用，但是命名为“_XX”的函数和变量不会被引入

# x_        与python关键词区分
#           如想定义一个class、def变量，可以写作class_
list_ = []
tuple_ = ()
dict_ = {}
set_ = set()

# __xx
#           self.__xx 它所命名的类成员确定无法被调用，但是可以通过函数调用
#           __xx 未通过self定义 在内 __xx | 类名._类名__xx  在外 类名._类名__xx
class test():
    def __method(self):
        return 42

    def call_it(self):
        return self.__method

print(test().call_it()())
# print(test().__method())
print(test()._test__method())

_test__method = 5
class test():
    def __init__(self):
        self.__method = 6

    def call_it(self):
        return self.__method

    def call_that(self):
        return __method

    def call_what(self):
        return _test__method

print(test()._test__method)  # 6
print(test().call_it())
print(test().call_that())
_test__method = 4
print(test().call_what())

# __xx__    内置特殊成员
#           内部约定的特殊命名，官方建议不要使用它们当作变量名
#           可以外部直接调用
