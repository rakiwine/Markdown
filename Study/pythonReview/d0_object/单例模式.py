# !/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/27
# file: 单例模式.py
# Email:
# Author: TSZ


# 主要目的是确保某一个类只有一个实例存在
# python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件

# __new__方法 方式实现单例
class Singleton_:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton_, cls).__new__(cls)
        return cls._instance


# 类方法 方式实现单例
class Player(object):
    # 静态变量
    _instanc = None
    _flag = False

    def __new__(cls, *args, **kwargs):
        print('new 执行')

        if cls._instanc is None:
            cls._instanc = super().__new__(cls)
        return cls._instanc

    def __init__(self):
        if not Player._flag:
            print('init')
            Player._flag = True

video = Player()
print(video)
music = Player()
print(music)

# 装饰器实现单例
def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kwagrs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwagrs)
        return _instance[cls]

    return _singleton

@Singleton
class A:
    a = 1

    def __init__(self, x=0):
        self.x = x

a1 = A(2)
a2 = A(4)
