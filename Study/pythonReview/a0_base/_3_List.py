#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/21
# file: _3_List.py
# Email:
# Author: rakiwine

_list = [[]]

count = 0
for item in dir(_list):
    if not item.startswith("_") and not item.startswith("__"):
        # print("Str.{}()".format(item))
        count += 1
# print(count)

# 作用 对第一层为深拷贝
# 参数
# 返回 None 不修改原列表
_list.copy()
# 浅拷贝 直接复制 for循环 切片 copy.copy
# 深拷贝 deepcopy.copy

# 作用 用新列表扩展原来的列表
# 参数 可迭代对象
# 返回 None 修改原列表
_list.extend([])

# 详解
# 作用 添加到列表末尾的对象。
# 参数 所有类型
# 返回 None 修改原列表
_list.append("param")

# 作用 将指定对象插入列表的指定位置
# 参数 索引 元素
# 返回 None 修改原列表
_list.insert(0, "")

# 作用 移除列表中的一个元素 默认最后一个元素
# 参数 索引 | 空
# 返回 移除的元素
_list.pop()

# 作用 移除列表中第一个匹配项 不存在抛出异常
# 参数 元素
# 返回 None 修改原列表
_list.remove("")

# 作用 清空列表list所有元素
# 参数
# 返回 None 修改原列表
_list.clear()

# 作用 统计某个元素在列表中出现的次数
# 参数 任意类型元素
# 返回 出现次数 不修改原列表
_list.count([])

# 作用 查找对象在区域出现位置 不存在抛出异常
# 参数 任意元素 起始位置 截止位置
# 返回 索引|异常 不修改原列表
_list.index("")

# 作用 反向列表中元素
# 参数
# 返回 None 修改原列表
_list.reverse()

# 实操

# 新建空列表
nullList = list()
null_list = []

#  新建非空列表
# 可以存放所有类型
notNullList = [1, 2.0, True, '你好', [1, 2], (1, 2), {1: 2}, {1, 2}, 1 + 2j]
not_nullList = list(i for i in range(1, 10))

# 可迭代对象包括 字符串 rang（） 列表 元组 文件
not_null_list = list('可迭代对象')

# 增加元素
notNullList.append('123')                   # 不改变首地址    在末尾增加字符串
notNullList.insert(1, '12')                 # 不改变首地址    在指定位置1 增加
notNullList.extend([1, 2])                  # 不改变首地址    在末尾增加可迭代对象
notNullList[len(notNullList):] = [123]      # 不改变首地址    在末尾增加可迭代对象


delList = []
# 删除列表 列表元素
del delList[1]                     # 删除列表位置1的元素
delList.pop(1)                     # 弹出列表位置1的元素   超出范围抛出异常
delList.pop()                      # 弹出列表尾部元素
delList.remove(1)                  # 移除首个出现的指定元素 不存在抛出异常
delList.clear()                    # 清空列表
del delList[::2]                   # 删除偶数位
del delList[:3]                    # 删除0 1 2 三个元素
delList[:3] = []		           # 删除前三个元素

# 修改
delList[1] = 4
delList[:3] = [1, 2, 3, 4]                  # 在0 - 1 - 2 上覆盖四个新元素
notNullList = notNullList + [4]             # 改变列表首地址   在末尾增加元素
notNullList = notNullList * 2               # 改变列表首地址   把当前列表复制拼接在一起

# 排序
delList.sort(reverse=True)             # 对于原列表排序 True 大到小 返回值为None
delList = sorted(delList)              # 改变列表首地址 返回新列表 小到大

# 列表翻转
delList.reverse()                      # 对于原列表翻转
delList = list(reversed(delList))      # 对列表翻转 返回迭代对象转换list对象

# 多列表打包元组 长度以最短为准
lis1 = [1, 2, 3]
lis2 = ['a', 'b', 'c']
lis3 = ['A', 'B', 'C']
zipped = zip(lis1, lis2, lis3)           # 可迭代的zip对象 返回的是迭代器
zipped = list(zipped)                    # 将迭代器装换为列表就可以在重复遍历
for i in zipped:
    print(i)
print(list(zipped))                      # 可迭代对象遍历之后为空
zip_p = list(zip(*zipped))

# 扁平化
lis0 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]  # 存在不可迭代对象将报错
lis1 = []
lis2 = []
lis3 = []
for i in lis0:
    lis1.extend(i)                      # 在末尾将可迭代对象依次加入
    lis2[len(lis2):] = i                # 在末尾长度上拼接
    lis3 = lis3 + list(i)               # 在末尾上拼接
print(lis1, lis2, lis3)

# 对列表函数
print(min(lis1))
print(max(lis1))
print(sum(lis1))
print(list(reversed(lis1)))             # 输入序列返回一个翻转的迭代器 转列表后输出
print(sorted(lis1))                     # 输入可迭代对象 返回一个新的list
print(type(delList))
print(list(zip(lis1, lis2)))
print(list(enumerate(lis1)))

# 拆包
a, b, c = [1, 2, 3]

# 列表推导式
delList = [i for i in range(10) for j in i if i > j]
