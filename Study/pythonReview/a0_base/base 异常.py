#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/23
# file: base 异常.py
# Email:
# Author: rakiwine 


# BaseException	所有异常的基类
# SystemExit	解释器请求退出
# KeyboardInterrupt	用户中断执行(通常是输入^C)
# Exception	常规错误的基类
# StopIteration	迭代器没有更多的值
# GeneratorExit	生成器(generator)发生异常来通知退出
# StandardError	所有的内建标准异常的基类
# ArithmeticError	所有数值计算错误的基类
# FloatingPointError	浮点计算错误
# OverflowError	数值运算超出最大限制
# ZeroDivisionError	除(或取模)零 (所有数据类型)
# AssertionError	断言语句失败
# AttributeError	对象没有这个属性
# EOFError	没有内建输入,到达EOF 标记
# EnvironmentError	操作系统错误的基类
# IOError	输入/输出操作失败
# OSError	操作系统错误
# WindowsError	系统调用失败
# ImportError	导入模块/对象失败
# LookupError	无效数据查询的基类
# IndexError	序列中没有此索引(index)
# KeyError	映射中没有这个键
# MemoryError	内存溢出错误(对于Python 解释器不是致命的)
# NameError	未声明/初始化对象 (没有属性)
# UnboundLocalError	访问未初始化的本地变量
# ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
# RuntimeError	一般的运行时错误
# NotImplementedError	尚未实现的方法
# SyntaxError	Python 语法错误
# IndentationError	缩进错误
# TabError	Tab 和空格混用
# SystemError	一般的解释器系统错误
# TypeError	对类型无效的操作
# ValueError	传入无效的参数
# UnicodeError	Unicode 相关的错误
# UnicodeDecodeError	Unicode 解码时的错误
# UnicodeEncodeError	Unicode 编码时错误
# UnicodeTranslateError	Unicode 转换时错误
# Warning	警告的基类
# DeprecationWarning	关于被弃用的特征的警告
# FutureWarning	关于构造将来语义会有改变的警告
# OverflowWarning	旧的关于自动提升为长整型(long)的警告
# PendingDeprecationWarning	关于特性将会被废弃的警告
# RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
# SyntaxWarning	可疑的语法的警告
# UserWarning	用户代码生成的警告

# 异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。
# 异常是Python对象，表示一个错误。
# 当Python脚本发生异常时我们需要捕获处理它，否则程序会终止执行。

# 开始一个try语句后，python就在当前程序的上下文中作标记，这样当异常出现时就可以回到这里
# try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句
# 没有匹配的except子句，异常将被递交到上层的try
# 如果在try子句执行时没有发生异常，python将执行else语句后的语句

# 断言 False 触发异常
assert 1 + 2

try:
    pass
except SystemExit:
    # 如果在try部份引发了'name'异常
    pass
except AssertionError as e:
    # 如果引发了'name'异常，获得附加的数据
    print(repr(e))
except (BaseException, IOError) as e:
    # 如果引发了'name'异常，获得附加的数据
    print(e)
    raise
    # raise BaseException('x 不能大于 5。x 的值为: {}'.format(5))
else:
    # 如果没有异常发生
    pass
finally:
    # 退出try时总会执行
    # 当在try块中抛出一个异常，立即执行finally块代码。finally块中的所有语句执行后，异常被再次触发，并执行except块代码。
    pass

# repr(e)       BaseException("error msg")      返回一个对象的 string 格式。
# try else finally
# try except 存在捕获 finally
# try except 不存在捕获 finally 报错


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):

        # eval(repr(obj)) == obj
        return repr(self)

try:
    raise MyError(2 * 2)
except MyError as e:
    print('My exception occurred, value:', e)
    print('My exception occurred, value:', e.value)
