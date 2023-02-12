#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/23
# file: 内置函数.py
# Email:
# Author: rakiwine 


# 内置函数字符串名列表获取
# dir(__builtins__)

count = 0
for item in dir(__builtins__):
    # if hasattr(item, "__call__"):
    objItem = eval(item)
    if callable(objItem) \
            and "Error" not in item \
            and not item.startswith("_") and not item.startswith("__") \
            and "Exception" not in item \
            and "Warning" not in item and "Iteration" not in item:
        # print("print('{0}', {0}())".format(item))
        print()
        count += 1
# print(count)


# type 不会认为子类是一种父类类型，不考虑继承关系
# isinstance 会认为子类是一种父类类型，考虑继承关系
print('isinstance', isinstance(count, int))
# X = type('X', (object,), dict(a=1)) 三个参数，返回新的类型对象
print('type', type(count))

# 执行一个字符串表达式，并返回表达式的值
print('eval', eval("print ('runoob.com ', end='')"))
print('exec', exec("print (string, end='')", dict(string="runoob.com ")))
# print('compile', compile())
# print('exit', exit())

# x 为纯数字，则不能有 a_base 参数
# 入参 x 取整
# x 为 str，则 a_base 可略可有
# a_base 存在时，视 x 为 a_base 类型数字，并将其转换为 10 进制数字
print('int', int())
# bool 是 int 的子类
print('bool', bool())
print('float', float())

print('abs', abs(-1))
# 返回一个包含商和余数的元组(a // b, a % b) divmod (1, 0)
print('divmod', divmod(1, 1))
# 计算 x 的 y 次方，如果 z 在存在，则再对结果进行取模
print('pow', pow(1, 1, 1))

print('all', all([0, 1, 0]))
print('any', any([0, 1, 0]))
print('sum', sum([0, 1, 0]))
# python2.x range() 函数可创建一个整数列表，一般用在 for 循环中
# Python3 range() 返回的是一个可迭代对象（类型是对象），打印的时候不会打印列表
print('range', range(10))
# 过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表
# Python2.7 返回列表，Python3.x 返回迭代器对象
print('filter', list(filter(lambda x: x, [])))

print('bin', bin(10))
# 将一个整数转换为一个八进制字符串
print('oct', oct(10))
# 将一个整数转换为一个十六进制字符串
print('hex', hex(10))

# 转义非 ASCII 字符： å \xe5
print('ascii str', ascii(["a", 1, "å"]))
# chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
print('chr', chr(65))
# 将一个字符作为参数，返回对应的 ASCII 数值转换为它的整数值 Unicode 字符超出了 Python 定义范围 引发一个 TypeError 的异常
print('ord', ord("A"))

# print('GeneratorExit', GeneratorExit())

# print('KeyboardInterrupt', KeyboardInterrupt())

# print('breakpoint', breakpoint())


# 数组里的元素是可变的，每个元素的值范围: 0 <= x < 256
# 如果 source 为整数，则返回一个长度为 source 的初始化数组；
# 如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
# 如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
# 如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
# 如果没有输入任何参数，默认就是初始化数组为0个元素。

# 返回一个新的 bytearray 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列
print('bytearray bytearray 10', bytearray(10))
print('bytearray bytearray "10"', bytearray("10", "utf-8"))
print('bytearray bytearray []', bytearray([0, 1, 255]))
print('bytearray bytearray 0', bytearray())
# 返回一个新的 bytearray 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列 它是 bytearray 的不可变版本
print('bytes bytes 10', bytes(10))
print('bytes bytes "10"', bytes("10", "utf-8"))
print('bytes bytes []', bytes([0, 1, 255]))
print('bytes bytes 0', bytes())

# 不带参数时，返回当前范围内的变量、方法和定义的类型列表
# 带参数时，返回参数的属性、方法列表
# 如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息
print('dir', dir())

# 可以通过 D.mro() (Python 2 使用 D.__mro__ ) 来查看 D 的 MRO 信息）
# Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx
# print('super', super())
# 在新式类中返回属性值
print('property', property())
# 判断参数 class 是否是类型参数 classinfo 的子类
print('issubclass', issubclass(count))

print('a0_complex', complex())

print('copyright', copyright())

print('credits', credits())

print('delattr', delattr())

print('dict', dict())

print('enumerate', enumerate())

print('format', format())

# 转换为不可变集合
print('frozenset', frozenset())

print('getattr', getattr())

print('globals', globals())

print('hasattr', hasattr())

print('hash', hash())

print('help', help())

print('id', id())


# 接受任意输入, 将所有输入默认为字符串处理,并返回字符串类型
# Python2.x
# raw_input() 将所有输入作为字符串看待，返回字符串类型
# input() 只能接收“数字”的输入，在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（ int, float ）。
# Python3.x
# 仅保留了 input( ) 函数，其接收任意任性输入，将所有输入默认为字符串处理，并返回字符串
print('input', input())

print('iter', iter())

print('len', len())

print('license', license())

print('list', list())

print('locals', locals())

print('map', map())

print('max', max())

print('memoryview', memoryview())

print('min', min())

print('next', next())

print('object', object())

print('open', open())

print('print', print())

print('quit', quit())

print('repr', repr())

print('reversed', reversed())

print('round', round())

print('set', set())

print('setattr', setattr())

print('slice', slice())

print('sorted', sorted())

print('staticmethod', staticmethod())

print('str', str())

print('tuple', tuple())

print('vars', vars())

print('zip', zip())
