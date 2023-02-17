#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/02/08
# file: _2_Format.py
# Email:
# Author: rakiwine

# { [index][ : [ [fill] align] [sign] [#] [width] [.precision] [type] ] }
# align <^>
# sign +-

# {{}}                       转义大括号
# {:b}                       {:b} b、d、#o、#x|X分别是二进制、十进制、八进制0o、十六进制0x
# {:s}                       字符串类型格式化
# {:c}                       将十进制整数自动转换成对应的 Unicode 字符。
# {: .2e}                    E\e 指数计数法(科学计数法)                 末位大于五 五舍五+入
# {: .2g}                    G\g 自动在 e 和 f（或 E 和 F）中切换。
# {:.2f}                     F\f {:.[保留位数][数据类型]}              四舍五+入 0 3 4 6 8
# {:+.2f}                    {:+.[保留位数][数据类型]} +显示+-|-显示-    四舍五+入 0 3 4 6 8
# {:.2%}                     百分数形式  保留两位小数                   整数奇入 四舍五入

# 位数不足{：.0}{：.1} 1.5 2e+00 | 1.4 1e+00
# {:.5}                      {:.截断宽度} 整数为0从小数算截断            整数偶入 四舍五入

# {:<5f} {:0^5f} {:x>5f}     {:[填充字符默认空格][<^>][宽度]} 不足字符填充|空格对齐
#                            =	数据右对齐，同时将符号放置在填充内容的最左侧，该选项只对数字类型有效


# {:,}                       千分位分隔符
# '{:%Y-%m-%d%H:%M:%S}'.format(date)   时间格式化

# 参数类型转换
def param_type_change():
    # 对参数使用str()
    print("   {!s}   ".format("ces"))
    #    ces
    # 对参数使用repr()
    print("   {!r}   ".format("ces"))
    #    'ces'


_dict = {
    "api": "cancelGame",
    "meth": "post",
    "data": {
        "gameId": "1234567890"
    }
}


# 控制参数位置
def control_param_index():
    # {}不能超过para个数
    try:
        print("{0} {2} {1} {}".format(0, 1, 2))
    except BaseException as e:
        pass

    # 列表/元组
    _list = [0, 1, 2]
    print('{0[0]} {0[2]} {0[1]}'.format(_list))
    print('{0} {2} {1}'.format(*_list))


# 按名称访问参数
def name_format():
    print("{age} {name}".format(name="name", age=18))

    # 字典
    _dict = {"name": "name", "age": 18}
    print('{_dict[age]} {_dict[name]}'.format(_dict=_dict))
    print("{age} {name}".format(**_dict))


# 通过参数属性访问
class AttributeFormat:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return'{self.a}  {self.b}'.format(self=self)


attributeFormat = AttributeFormat(1, 2)
# str(attributeFormat)
# print('{attributeFormat.a}  {attributeFormat.b}'.format(attributeFormat=attributeFormat))






