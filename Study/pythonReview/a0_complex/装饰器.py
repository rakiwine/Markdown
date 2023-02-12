#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/23
# file: 装饰器.py
# Email:
# Author: rakiwine


# 什么是装饰器呢？
# 就是在特定条件下为某些函数再不改动函数体的时候为函数新添加一些功能，这就是装饰器
#
#  实现原理：
# 基于@语法和函数闭包，将原函数封装在闭包中，然后将函数赋值为一个新的函数（内置函数），执行函数时再在内层函数中执行闭包中的原函数
#
# 实现效果：
# 可以在你改变函数内部代码和调用的前提下，实现在函数执行和执行拓展功能
#
# 适用场景：
# 多个函数系统统一在执行前后定义一些功能

# 在被装饰对象正上方的单独一行写@装饰器名字

import functools


def outer(origin):
    @functools.wraps(origin)
    def inner(*args, **kwargs):
        print("装饰器的学习 1")

        res = origin(*args, **kwargs)

        print("装饰器的学习 2")

        return res

    return inner

# ces=outer(ces)
@outer
def ces(x, y, z):
    # 我是个函数
    print("我是三函数")


ces(4, 5, 6)
print(ces.__name__)
print(ces.__doc__)
