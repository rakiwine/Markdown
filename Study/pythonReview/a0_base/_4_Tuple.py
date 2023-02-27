#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/21
# file: _4_Tuple.py
# Email:
# Author: rakiwine

_tuple = tuple()

# 作用 统计某个元素在元组中出现的次数
# 参数 任意类型元素
# 返回 出现次数 不修改原列表
_tuple.count([])

# 作用 查找对象在区域出现位置 不存在抛出异常
# 参数 任意元素 起始位置 截止位置
# 返回 索引|异常 不修改原列表
_tuple.index("")

# 实操

# 元组内容不可修改 删改查 截取[:] 组合+*
# 元组优点 速度比列表快 元组可作为字典key 返回值
# 新建空元祖
_tuple = tuple()             # 无意义
_tuple = ()

# 新建非空元祖 可以存放所有类型
_tuple = (3,)                # ,防止不识别为元祖
_tuple = (1, 2.0, True, '你好', [1, 2], (1, 2), {1: 2}, {1, 2}, 1 + 2j)
_tuple = tuple(i for i in range(1, 10))

# 可迭代对象包括 字符串 range() 列表 文件
_tuple = tuple('可迭代对象')

# 增加元素 不可修改

# 删除元组
del _tuple

# 修改元组 组合+*
_tuple = _tuple + _tuple
_tuple = _tuple * 2