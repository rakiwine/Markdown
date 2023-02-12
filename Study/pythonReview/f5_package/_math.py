#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/22
# file: _math.py
# Email:
# Author: rakiwine

import math

int_z_num = 9.0
int_f_num = -9
float_z_num = 12.21
float_f_num = -21

count = 0
for item in dir(math):
    if not item.startswith("_") and not item.startswith("__"):
        # print("math.{}()".format(item))
        count += 1
# print(count)

# 作用 abs 返回int/float绝对值 fabs 返回int/float的 float类型绝对值
# 返回 新的数值
# 结果 不改变原数值
print(abs(int_f_num), int_f_num)
print(math.fabs(int_f_num), int_f_num)

min()
max()
round()

#  (x>y)-(x<y)
math.ceil()
math.floor()
math.pow()
math.exp()
math.modf()

# 作用 返回一个原字符串居中
# 返回 新的字符串
# 结果 不改变原字符串
print(math.sqrt(2, 3))

math.acos()
math.acosh()
math.asin()
math.asinh()
math.atan()
math.atan2()
math.atanh()
math.copysign()
math.cos()
math.cosh()
math.degrees()
math.e()
math.erf()
math.erfc()
math.expm1()
math.factorial()
math.fmod()
math.frexp()
math.fsum()
math.gamma()
math.gcd()
math.hypot()
math.inf()
math.isclose()
math.isfinite()
math.isinf()
math.isnan()
math.ldexp()
math.lgamma()
math.log()
math.log10()
math.log1p()
math.log2()
math.nan()
math.pi()
math.radians()
math.remainder()
math.sin()
math.sinh()
math.tan()
math.tanh()
math.tau()
math.trunc()