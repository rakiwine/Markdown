#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/23
# file: 迭代器与生成器.py
# Email:
# Author: rakiwine

# for循环处理 将可迭代对象转换为迭代器取值
# for循环他们返回的一个迭代器对象，这些迭代器对象只能迭代一次

# 可迭代对象 列表 元组 字符串 字典 集合 生成器
#       本质 具备__iter__ 的对象
#       优点 可以直观看见里面的数据
#       缺点 占用内存

# 迭代器 文件对象
#       本质 含有 __iter__ __next__ 的对象
#       优点 节省内存 惰性取值
#       缺点 不能直观看见里面的数据 只能next一直往后取

# 可迭代对象转迭代器
iter([])

# 异常
# 取完之后会报StopIteration错


# 生成器
# 1.生成器本身是一种特殊的迭代器，也就是说生成器就是迭代器。
#
# 2.生成器会自动实现迭代器协议，也就是说只要我们yield后，自动就生成了next对象包括StopIteration等结构。
#
# 3.生成器使用yield语句返回一个值。yield语句挂起该生成器函数的状态，保留足够的信息。
# 对生成器函数的第二次（或第n次）调用，跳转到函数上一次挂起的位置。生成器不仅“记住”了它的数据状态，生成还记住了程序执行的位置。
def generator(n):
    for i in range(n):
        yield i ** 2


genera = generator(3)
print(genera)
print(next(genera))
# 生成器推导式
print(i for i in range(100000000))


def test_yield_from(*iterables):
    for i in iterables:
        for j in i:
            yield j


print(test_yield_from())
print(list(test_yield_from([1, 2, 3], 'abc')))

# 生成器与迭代器区别
# 迭代器是从有到有的复制，生成器是从无到有的生成
# 生成器是实现自己独有方法的迭代器，我们可以把他看成迭代器的子类
