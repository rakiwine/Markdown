#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/21
# file: _3_List.py
# Email:
# Author: rakiwine

_list = []

count = 0
for item in dir(_list):
    if not item.startswith("_") and not item.startswith("__"):
        # print("Str.{}()".format(item))
        count += 1
# print(count)

# 详解
# 作用 添加到列表末尾的对象。
# 参数 所有类型
# 返回 None
_list.append("param")

# 实操
# 新建空列表
lis_null1 = list()
lis_null2 = []

# 新建非空列表 可以存放所有类型
lis_notnull1 = [1, 2.0, True, '你好', [1, 2], (1, 2), {1: 2}, {1, 2}, 1+2j]
# 可迭代对象包括 字符串 rang（） 列表 元组 文件
lis_notnull2 = list('可迭代对象')
lis_notnull3 = list(i for i in range(1, 10))

lis_add = []


# 增加元素
lis_add.append('123')               # 不改变首地址    在末尾增加字符串
lis_add.insert(1, '12')             # 不改变首地址    在指定位置1 增加
lis_add.extend([1, 2])              # 不改变首地址    在末尾增加可迭代对象
lis_add[len(lis_add):] = [123]      # 不改变首地址    在末尾增加可迭代对象
lis_add = lis_add + [4]             # 改变列表首地址   在末尾增加元素
lis_add = lis_add * 2               # 改变列表首地址   把当前列表复制拼接在一起

lis = []
# 删除列表 列表元素
del lis[1]                     # 删除列表位置1的元素
lis.pop(1)                     # 弹出列表位置1的元素   超出范围抛出异常
lis.pop()                      # 弹出列表尾部元素
lis.remove(1)                  # 移除首个出现的指定元素 不存在抛出异常
lis.clear()                    # 清空列表
del lis[::2]                   # 删除偶数位
del lis[:3]                    # 删除0 1 2 三个元素
lis[:3]=[]		       # 删除前三个元素

# 修改
lis[1] = 4
lis[:3] = [1, 2, 3, 4]        # 在0 - 1 - 2 上覆盖四个新元素

# 查询
lis.count(1)                   # 查询列表中1的个数 不存在返回0
lis.index(1, 0, len(lis))      # 查询从start到end位置的1的下标 不存在返回异常
i = (1 in lis)                 # 存在返回 True 否则返回 flase

# 排序
lis.sort(reverse=True)         # 对于原列表排序 True 降序排列 返回值为None
lis = sorted(lis)              # 改变列表首地址 返回新列表

# 列表翻转
lis.reverse()                  # 对于原列表翻转
lis = list(reversed(lis))      # 对列表翻转 返回迭代对象转换list对象

# 字符串转列表
lis_str = list('asdf')

# 元组转列表
tup = (1, 2, 3, 4)
lis_tup = list(tup)

# 多列表打包元组 长度以最短为准
lis1 = [1, 2, 3]
lis2 = ['a', 'b', 'c']
lis3 = ['A', 'B', 'C']
zipped = zip(lis1, lis2, lis3)           # 可迭代的zip对象 返回的是迭代器
zipped = list(zipped)                    # 将迭代器装换为列表就可以在重复遍历
for i in zipped:
    print(i)
print(list(zipped))                      # 遍历之后为空
zip_p = list(zip(*zipped))


# 枚举
for i, v in enumerate(lis1):             # 遍历枚举
    print(i, v)

print(list(enumerate(lis1)))             # 转换为枚举对象再转换列表

# 扁平化
lis0 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]  # 存在不可迭代对象将报错
lis1 = []
lis2 = []
lis3 = []
for i in lis0:
    lis1.extend(i)                      # 在末尾将可迭代对象依次加入
    lis2[len(lis2):] = i                #
    lis3 = lis3 + list(i)               #
print(lis1, lis2, lis3)

# 对列表函数
print(min(lis1))
print(max(lis1))
print(sum(lis1))
print(list(reversed(lis1)))             # 输入序列返回一个翻转的迭代器 转列表后输出
print(sorted(lis1))                     # 输入可迭代对象 返回一个新的list
print(type(lis))
print(list(zip(lis1, lis2)))
print(list(enumerate(lis1)))

# 遍历
for i in lis1:
    pass

for i in range(len(lis1)):
    pass

for i, v in enumerate(lis1):
    pass

# 拆包
a, b, c = [1, 2, 3]

# 列表推导式
lis = [i for i in range(10)]
lis = [i for i in range(10) for j in i if i > j]


# 列表切片
print(lis[::-1])
print(lis[:])
# [start: end: sep] start + sep -> end 能够前进才存在值