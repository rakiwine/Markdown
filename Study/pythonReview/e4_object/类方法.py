#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/27
# file: 类方法.py
# Email:
# Author: TSZ

#!/usr/bin/env python
#-*- coding:utf-8 -*-

class People(object):
    def __init__(self):
        self.name = 'Tom'
        self.age = 23

    def commonFunc(self):       # 定义公有方法
        pass

    def __privateFunc(self):    # 定义私有方法
        pass

    @classmethod                # 定义类方法 调用类的属性
    def classFunc(cls):
        pass

    @staticmethod               # 定义静态方法，注意没有self参数
    def staticFunc():
        pass

    def test(self):
        self.commonFunc()       # 可以在类的内部调用公有方法
        self.__privateFunc()    # 可以在类的内部调用私有方法
        self.classFunc()        # 可以在类的内部调用类方法
        self.staticFunc()       # 可以在类的内部调用静态方法

if __name__ == '__main__':
    obj = People()
    obj.commonFunc()       # 可以通过对象在类的外部调用公有方法
    # obj.__privateFunc()    # 不可以通过对象在类的外部调用私有方法，这里会报错
    obj.classFunc()        # 可以通过对象在类的外部调用类方法
    obj.staticFunc()       # 可以通过对象在类的外部调用静态方法


    # 与类和实例无绑定关系的 function 都属于函数
    # 与类和实例有绑定关系的 function 都属于方法    类的静态方法是函数