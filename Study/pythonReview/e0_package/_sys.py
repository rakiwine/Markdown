#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/21
# file: _sys.py
# Email:
# Author: rakiwine 


import os
import sys

count = 0

for item in dir(sys):
    if not item.startswith("_") and not item.startswith("__"):
        # print("print('sys.{0}', sys.{0}())".format(item))
        count += 1
# print(count)

# append()方法可以新增模块目录
# python xxx.py
# python -m xxx.py
# 1叫做直接运行
# 2把模块当作脚本来启动(注意：但是__name__的值为'main' )
# 导入一个叫 mod1 的模块时，解释器先在当前目录中搜索名为 mod1.py 的文件。如果没有找到的话，接着会到 sys.path 变量中给出的目录列表中查找。
# 主程序文件应该在最外层
print('sys.path', sys.path)

# 这是通过引发SystemExit 异常来实现的，
# 因此遵循finally语句的子句所指定的清理操作try ，
# 并且可以拦截外层的退出尝试。
# 默认为零 大多数系统要求它在0-127范围内
# 如果它是整数，则零被认为是“成功终止”，并且任何非零值被贝壳等视为“异常终止”。
# print('sys.exit', sys.exit())

# 只能实现退出子线程
# sys.exit()
# exit()
# quit()

# 子线程中调用os._exit，可以实现整个程序的退出
os._exit(0)

# 传参，第一个参数为脚本名称即argv[0]
print('sys.argv', sys.argv)

# sys.modules是一个全局 {字典}，该字典是python启动后就加载在内存中
# 导入新的模块时，sys.modules记录新模块
# 可以被操纵以强制重新加载模块和其他技巧。
print('sys.modules', sys.modules)

# 返回对象的引用计数。
print('sys.getrefcount', sys.getrefcount(count))

# 包含与Python解释器相关的版权的字符串
print('sys.copyright', sys.copyright)

# 返回系统平台名称
print('sys.platform', sys.platform)
# 查看python版本
print('sys.version', sys.version)
# 此解释器的C API版本
print('sys.api_version', sys.api_version)
# 包含版本号的五个组件的元组：major，minor， micro，releaselevel和serial。
print('sys.version_info', sys.version_info)

# 用于在Windows平台上形成注册表项的版本号。
# 它作为字符串资源1000存储在Python DLL中。 3.7
print('sys.winver', sys.winver)

# 返回一个描述当前正在运行的Windows版本的命名元组。
print('sys.getwindowsversion', sys.getwindowsversion())

# 标准unix输入 类文件流对象
# 丢弃/n
# stdin_str = sys.stdin.readline()[:-1]
# input_str = input()
# print('Hello ', stdin_str, input_str)

# 标准unix输出 类文件流对象
# f_handler = open('out.log', 'w')
# sys.stdout = f_handler
print('sys.stderr', sys.stderr)
print('sys.stdin', sys.stdin)
print('sys.stdout', sys.stdout)
# sys.stdout.flush()

# 平台的Py_ssize_t类型支持的最大正整数
print('sys.maxsize', sys.maxsize)
# 最大的Unicode值
print('sys.maxunicode', sys.maxunicode)
# 版本号编码为单个整数。16进制格式
print('sys.hexversion', sys.hexversion)

# 返回平台独立的python文件安装的位置
# D:\ProgramData\Anaconda3\envs\fast_product
# /usr/local
print('sys.exec_prefix', sys.exec_prefix)
print('sys.prefix', sys.prefix)

# 给出Python解释器的可执行二进制文件的绝对路径
# D:\ProgramData\Anaconda3\envs\fast_product\python.exe
print('sys.executable', sys.executable)

# 检查间隔 如 线程切换和信号处理程序的频率
print('sys.getcheckinterval', sys.getcheckinterval)
print('sys.getcheckinterval', sys.setcheckinterval(100))

# 返回递归限制的当前值，即Python解释器堆栈的最大深度。
print('sys.getrecursionlimit', sys.getrecursionlimit())
# 设置Python解释器堆栈的最大深度以限制
print('sys.setrecursionlimit', sys.setrecursionlimit(10))

# 返回Unicode实现使用的当前默认字符串编码的名称。 utf-8
print('sys.getdefaultencoding', sys.getdefaultencoding())
# 返回用于将Unicode文件名转换为系统文件名的None编码名称 utf-8
print('sys.getfilesystemencoding', sys.getfilesystemencoding())

# 以字节为单位返回对象的大小。
# 但这不一定适用于第三方扩展，因为它是特定于实现的。
# print('sys.getsizeof', sys.getsizeof(sys))

# 在程序的开始 这些对象包含的原始值displayhook和excepthook
# sys.__displayhook__ displayhook()函数的初始值。
# print(sys.__displayhook__())
# print('sys.displayhook', sys.displayhook(1))

# 如果object不是None，则此函数将他保存进__builtin__._.指在python的交互式解释器里，'_' 代表上次你输入得到的结果
# print('sys.displayhook', sys.displayhook(object))

# sys.__excepthook__ excepthook()函数的初始值。
# print(sys.__excepthook__())
# sys.excepthook()
# 是为python交互式解释器之类的东西设计的 打印异常并返回到交互式shell 异常类，异常实例和回溯对象
# print('sys.excepthook', sys.excepthook(exctype, value, traceback))

# (None, None, None)
# type获取正在处理的异常的异常类型（类对象）
# value获取异常参数（其 关联值或第二个参数，如果异常类型是类对象，则始终为类实例）
# traceback 获取一个回溯对象
# print('sys.exc_info', sys.exc_info())

# 这是警告框架的实现细节; 不要修改此值。
# print('sys.warnoptions', sys.warnoptions)

# 指定Python DLL句柄的整数
print('sys.dllhandle', sys.dllhandle)

# 本机字节顺序的指示符。大端小端
print('sys.byteorder', sys.byteorder)

# 获取设置的探查器功能setprofile
# print('sys.getprofile', sys.getprofile())

# 获取设置的跟踪功能set trace
# print('sys.gettrace', sys.gettrace())
# 跟踪函数应该有三个参数：frame，event和 arg。frame是当前的堆栈帧。
# 事件是一个字符串：’call’， ‘line’，’return’或’exception’。 arg取决于事件类型。
# print('sys.settrace', sys.settrace())

# 如果这是真的，Python将不会尝试在源模块的导入上编写.pyc或.pyo文件。
# 此值最初设置为True或 False取决于-B命令行选项和 PYTHONDONTWRITEBYTECODE 环境变量
# print('sys.dont_write_bytecode', sys.dont_write_bytecode)

# 清除内部类型缓存。类型缓存用于加速属性和方法查找。
# 为了优化方法查询, 在解释器内部保留了1024项最近所用方法的缓存。
# 该缓存加快了对重复方法的查询——特别是在具有深层继承层次结构的代码中。
# 通常不必清空该缓存,但是如果要跟踪真正复杂的内存引用计数问题, 就可以这么做。
# 例如, 如果缓存中的方法要保留准备销毁的对象的引用时。
print('sys._clear_type_cache', sys._clear_type_cache())

# 返回一个字典，将每个线程的标识符映射到调用该函数时该线程中当前活动的最顶层堆栈帧
# print('sys._current_frames', sys._current_frames())

# 一个字符串元组，给出了编译到此Python解释器中的所有模块的名称。
print('sys.builtin_module_names', sys.builtin_module_names)

# call func(*args)，同时启用跟踪。跟踪状态被保存，然后恢复。这是从调试器从检查点调用，以递归调试其他一些代码。
# print('sys.call_tracing', sys.call_tracing(func, args=(,)))

# struct sequence 标志公开命令行标志的状态。属性是只读的。
# print('sys.flags', sys.flags)

# struct seq保存有关float类型的信息。它包含有关精度和内部表示的低级信息。
# print('sys.int_info', sys.int_info)
# print('sys.hash_info', sys.hash_info)
# print('sys.float_info', sys.float_info)
# print('sys.thread_info', sys.thread_info)

# 指示repr()函数对浮点数的行为方式。
# 如果字符串具有值，’short’则对于有限浮点数x，repr(x)旨在生成具有该属性的短字符串。
# print('sys.float_repr_style', sys.float_repr_style)

# 调用其方法的finder对象列表，find_module()以查看其中一个对象是否可以找到要导入的模块。
# [
#     <class '_frozen_importlib.BuiltinImporter'>,
#     <class '_frozen_importlib.FrozenImporter'>,
#     <class '_frozen_importlib_external.PathFinder'>
# ]
# print('sys.meta_path', sys.meta_path)

# 设置系统的配置文件功能
# 系统的配置文件函数的调用类似于系统的跟踪函数
# print('sys.setprofile', sys.setprofile())

# 一个callables列表，它采用path参数来尝试为路径创建 finder。
# [
#   <class 'zipimport.zipimporter'>,
#   <function FileFinder.path_hook.<locals>.path_hook_for_FileFinder at 0x000001F22967CE58>
# ]
# print('sys.path_hooks', sys.path_hooks)

# {
#     'D:\\hin-now_work\\fast_product': FileFinder('D:\\hin-now_work\\fast_product'),
#     'C:\\Program Files\\JetBrains\\PyCharm 2019.1.2\\helpers\\pycharm_matplotlib_backend': FileFinder('C:\\Program Files\\JetBrains\\PyCharm 2019.1.2\\helpers\\pycharm_matplotlib_backend'),
#     'C:\\Program Files\\JetBrains\\PyCharm 2019.1.2\\helpers\\pycharm_display': FileFinder('C:\\Program Files\\JetBrains\\PyCharm 2019.1.2\\helpers\\pycharm_display'),
#     'D:\\ProgramData\\Anaconda3\\envs\\fast_product\\python37.zip': None,
#     'D:\\ProgramData\\Anaconda3\\envs\\fast_product\\DLLs': FileFinder('D:\\ProgramData\\Anaconda3\\envs\\fast_product\\DLLs'),
#     'D:\\ProgramData\\Anaconda3\\envs\\fast_product\\lib': FileFinder('D:\\ProgramData\\Anaconda3\\envs\\fast_product\\lib'),
#     'D:\\ProgramData\\Anaconda3\\envs\\fast_product\\lib\\encodings': FileFinder('D:\\ProgramData\\Anaconda3\\envs\\fast_product\\lib\\encodings'),
#     'D:\\ProgramData\\Anaconda3\\envs\\fast_product': FileFinder('D:\\ProgramData\\Anaconda3\\envs\\fast_product'),
#     'D:\\ProgramData\\Anaconda3\\envs\\fast_product\\lib\\site-packages': FileFinder('D:\\ProgramData\\Anaconda3\\envs\\fast_product\\lib\\site-packages'),
#     'D:\\ProgramData\\Anaconda3\\envs\\fast_product\\lib\\site-packages\\win32': FileFinder('D:\\ProgramData\\Anaconda3\\envs\\fast_product\\lib\\site-packages\\win32'),
#     'D:\\ProgramData\\Anaconda3\\envs\\fast_product\\lib\\site-packages\\win32\\lib': FileFinder('D:\\ProgramData\\Anaconda3\\envs\\fast_product\\lib\\site-packages\\win32\\lib'),
#     'D:\\ProgramData\\Anaconda3\\envs\\fast_product\\lib\\site-packages\\Pythonwin': FileFinder('D:\\ProgramData\\Anaconda3\\envs\\fast_product\\lib\\site-packages\\Pythonwin'),
#     'D:/hin-now_work/fast_product/f_package/ces.py': None
# }
# 充当查找程序对象缓存的字典。键是已传递到的路径
# print('sys.path_importer_cache', sys.path_importer_cache)

# print('sys.intern', sys.intern())
# print('sys.callstats', sys.callstats())
# print('sys.breakpointhook', sys.breakpointhook())
# print('sys.implementation', sys.implementation)
# print('sys.is_finalizing', sys.is_finalizing())
# print('sys.getallocatedblocks', sys.getallocatedblocks())
# print('sys.getfilesystemencodeerrors', sys.getfilesystemencodeerrors())

# print('sys.base_prefix', sys.base_prefix)
# print('sys.base_exec_prefix', sys.base_exec_prefix)

# print('sys.getswitchinterval', sys.getswitchinterval())
# print('sys.setswitchinterval', sys.setswitchinterval())

# print('sys.get_asyncgen_hooks', sys.get_asyncgen_hooks())
# print('sys.set_asyncgen_hooks', sys.set_asyncgen_hooks())

# print('sys.set_coroutine_wrapper', sys.set_coroutine_wrapper())
# print('sys.get_coroutine_wrapper', sys.get_coroutine_wrapper)
# print('sys.get_coroutine_origin_tracking_depth', sys.get_coroutine_origin_tracking_depth())
# print('sys.set_coroutine_origin_tracking_depth', sys.set_coroutine_origin_tracking_depth)

