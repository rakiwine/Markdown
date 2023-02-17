#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/02/08
# file: _2_Percent.py
# Email:
# Author: rakiwine

# format_spec     =  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
# fill            =  <any character>
# align           =  "<" ，">"，"="，"^"
# sign            =  "+"，"-"，" "
# width           =  digit+
# grouping_option =  "_"，","
# precision       =  digit+
# type            =  "b"，"c"，"d"，"e"，"E"，"f"，"F"， "g"，"G"，"n"，"o"，"s"，"x"， "X"，"%"
Str = f"{1+1}"

# %[(key)][flags][width].[precision]typecode
# %（key）		    用于字典
# flags		        +-''
# width		        宽度
# precision	        小数点后精度

# %%                转义百分号

# %s|r              格式化字符串 str|repr
# %(key)typecode    输出对应字典key对应的value
print("%(key)s" % {"key": "value"})

# %c        格式化字符及其ASCII码
print("%c" % "A")
print("%c %c" % (97, 65))

# %d|i    负数有符号    格式化整数
# %u      负数有符号	  格式化无符号整型
# %o      负数有符号    格式化无符号八进制数
# %x|X    负数有符号    格式化无符号十六进制数
# %e|E    负数有符号    用科学计数法格式化浮点数
# %f      负数有符号    格式化浮点数

# %p      用十六进制数格式化变量的地址
print("未找到用法实例")

# %g      负数有符号   大数%e|小数%f 四舍五+入
# %G      %F 和 %E 的简写
print("%g" % 0.55555551)

# %n 	  存储输出字符的数量放进参数列表的下一个变量中
print("未找到用法实例")

# %8	  规定宽度
# %-08f   左对齐 右填充0
# %08.4f  右对齐 左填充0
print("%-08f" % 0.5555)
print("%08.4f" % 0.5555)

# *	      定义宽度或者小数点精度
# %+	  显示+-号
# <sp>	  在正数前面显示空格
# %#	  对于进制 0o 0x 0X 的显示
# %0      显示的数字前面填充'0'而不是默认的空格
# m.n	  m 宽度,n 小数点后的位数
