#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/02/08
# file: _2_Format.py
# Email:
# Author: rakiwine

# 转义大括号            {{}}
# 对齐                 {:[填充字符默认空格][<^>][宽度]} {:<5} {:^5} {:>5}
# 截断                 {:.截断宽度} {:.5}
# 保留两位小数 四舍五入   {:.2%}
# 格式化               {:.[保留位数][数据类型]} {:.2f}
# 千分位分隔符           {:,}
# 时间格式化            '{:%Y-%m-%d%H:%M:%S}'.format(date)

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






