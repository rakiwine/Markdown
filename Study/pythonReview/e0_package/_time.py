#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/02/26
# file: _time.py
# Email:
# Author: rakiwine

"""
%Y 四位数的年份表示（000-9999） %y 两位数的年份表示（00-99）
%m 月份（01-12）
%d 月内中的一天（01-31）

%H 24小时制小时数（00-23）      %I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）

%p 本地A.M.或P.M.的等价符

%a 本地简化星期名称
%A 本地完整星期名称

%b 本地简化的月份名称
%B 本地完整的月份名称

%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）

%U 一年中的星期数（00-53）星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始

%w 星期（0-6），星期天为星期的开始

%x 本地相应的日期表示
%X 本地相应的时间表示

%Z 当前时区的名称
%% %号本身
"""

import time


# 作用 返回时间戳 time()精度上相对没有那么高，而且受系统的影响，适合表示日期时间或者大程序程序的计时。
# 参数
# 返回 float类型6位小数
_time = time.time()


# 作用 延迟运行单位为s
# 参数 float类型
# 返回 None
time.sleep(1.11)

# 作用 将时间对象转换为规范性字符串
# 参数 格式化字符串, struct_time对象没有微秒|时区
# 返回 时间字符串
time.strftime("%Y-%m-%d %H:%M:%S", time.struct_time((2020, 12, 3, 11, 3, 3, 0, 211, 0)))

# 作用 将 时间字符串 根据 格式化字符串 转换成 时间数组
# 参数 时间字符串，格式化字符串
# 返回 struct_time对象没有微秒|时区
time.strptime("2023-02-11 00:00:01.000001+00:00", "%Y-%m-%d %H:%M:%S.%f%z")


# 缩减时间字符串
def _asctime():
    # 作用 转换时间戳为本地时间对象 本地时间
    # 参数 无参数
    # 返回 struct_time类型 当前时间元组
    # 参数 float类型 返回1970开始的时间元组对象
    # 返回 struct_time类型
    time.localtime()

    # 作用 将本地时间转换为时间戳
    # 参数
    # 返回 float类型
    time.mktime(time.localtime())

    # 作用 转换时间戳为时间元组（时间对象） utc时间 + 8 = 本地时间
    # 参数 无参数
    # 返回 struct_time类型 当前时间元组
    # 参数 float类型 返回1970开始的时间元组对象
    # 返回 struct_time类型
    time.gmtime()

    # 作用 将时间对象转换为缩减时间字符串
    # 参数 无参 | time.localtime() | time.gmtime()
    # 参数 年，月，日，时，分，秒，星期，第几天，夏令时。(2020,12,3,11,3,3,0,211,0)
    # 返回 str类型 Sun Feb 26 15:11:50 2023
    time.asctime()

    # 作用 将时间戳转换为缩减时间字符串
    # 参数 float类型
    # 返回
    time.ctime()
    # 等价于 asctime(localtime(secs))


# 作用
# 参数 "clock" "monotonic" "time" "perf_counter" "process_time" "thread_time"
# 返回 SimpleNamespace 名称空间对象(
#   adjustable: 如果系统管理员可以自动或手动更改时钟，则为“ True”。否则为“假”。
#   implementation: 用于获取时钟值的基础C函数的名称。
#   monotonic: 如果时钟不能倒退，则该值为true。否则为假。
#   resolution: 此属性以秒为单位指定时钟的分辨率。
# )
time.get_clock_info("")

# 3.3启用 3.8移除


def _clock():
    # 作用
    # 参数
    # 返回
    # time.clock()

    # 作用 获取一个单调时钟的值
    # 参数
    # 返回
    time.monotonic()

    # 作用 获取一个单调时钟的值
    # 参数
    # 返回
    time.monotonic_ns()

    # 作用 返回时间戳 time() 精度上相对没有那么高，而且受系统的影响，适合表示日期时间或者大程序程序的计时。
    # 参数
    # 返回 float类型6位小数
    time.time()

    # 作用 返回时间戳 time()
    # 参数
    # 返回 int 1677397038900950700
    time.time_ns()

    # 作用 返回以秒为单位的时间浮点值 会包含sleep()休眠时间，适用测量短持续时间
    # 参数
    # 返回 float 0.0419379
    time.perf_counter()

    # 作用 函数以纳秒为单位给出时间的整数值。
    # 参数
    # 返回 int 47346000
    time.perf_counter_ns()

    # 作用 返回系统的当前时间和用户CPU时间的浮动值(以秒为单位) 不包括sleep()休眠时间期间经过的时间。
    # 参数
    # 返回 float 0.0
    time.process_time()

    # 作用 返回系统的当前时间和用户CPU时间的浮动值(以纳秒为单位)
    # 参数
    # 返回 int 15625000
    time.process_time_ns()

    # 作用 获取当前线程|进程的CPU时间(不含休眠)
    # 参数
    # 返回
    time.thread_time()

    # 作用 获取当前线程|进程的CPU时间(不含休眠)
    # 参数
    # 返回
    time.thread_time_ns()


# 返回 int类型 返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值
time.altzone

# 返回 int类型 数在定义夏令时 (DST) 时返回非零整数值，否则返回 0
time.daylight

# 返回
time.tzname

# 返回 int类型
time.timezone

# 作用
# 参数 时间元组(2020,12,3,11,3,3,0,211,0)
# 返回 struct_time类型
time.struct_time((2020, 12, 3, 11, 3, 3, 0, 211, 0))
