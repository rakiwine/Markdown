#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/02/11
# file: _datetime.py
# Email:
# Author: rakiwine

import datetime

# 1 <= year <= 9999
# 1 <= month <= 12
# 1 <= day <= 给定年月对应的天数
# 0 <= hour < 24
# 0 <= minute < 60
# 0 <= second < 60
# 0 <= microsecond <1000,000
# tzinfo 默认None tzinfo 子类的实例
# fold in [0, 1] 默认0 文档无描述
_datetime = datetime.datetime(year=2023, month=2, day=11, hour=0, minute=0, second=0, microsecond=0)

_date = datetime.date(year=2023, month=2, day=11)
# _date.year, _date.month, _date.day

_time = datetime.time(hour=0, minute=0, second=0, microsecond=0)
# _time.hour, _time.minute, _time.second, _time.microsecond, _time.tzinfo, _time.fold

_tzinfo = datetime.tzinfo()

# milliseconds 1000     毫秒
# microseconds 1000,000 微秒
_timedelta = datetime.timedelta(weeks=1, days=1, hours=1, minutes=1, seconds=1, milliseconds=1, microseconds=1)
# _timedelta.days _timedelta.microseconds _timedelta.seconds

count = 0
# for item in dir(_datetime):
# for item in dir(_date):
# for item in dir(_time):
# for item in dir(_tzinfo):
for item in dir(_timedelta):
    if not item.startswith("_") and not item.startswith("__"):
        # print("_datetime.{}()".format(item))
        # print("_date.{}()".format(item))
        # print("_time.{}()".format(item))
        # print("_tzinfo.{}()".format(item))
        # print("_timedelta.{}()".format(item))
        count += 1

# print(count)


"""
%Y 四位数的年份表示（000-9999）              %y 两位数的年份表示（00-99）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）                   %I 12小时制小时数（01-12）
%M 分钟数（00-59）
%S 秒（00-59）
%A 本地完整星期名称                         %a 本地简化星期名称
%B 本地完整的月份名称                       %b 本地简化的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%w 星期（0-6），星期天为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
"""


# date time datetime 转字符串格式化
def object_to_str():
    def _strftime():
        # 2023-02-11 00:00:01.000001
        _datetime.strftime("%Y-%m-%d %H:%M:%S.%f%z")
        # 00:00:00.000000
        _time.strftime("%H:%M:%S.%f%z")
        # 2023-02-11
        _date.strftime("%Y-%m-%d")

    def _isoformat():
        # timespec 时间规格
        #     'hours': '{:02d}',
        #     'minutes': '{:02d}:{:02d}',
        #     'seconds': '{:02d}:{:02d}:{:02d}',
        #     'milliseconds': '{:02d}:{:02d}:{:02d}.{:03d}',
        #     'microseconds': '{:02d}:{:02d}:{:02d}.{:06d}'

        # 2023-02-11T00:00:01.000001
        _datetime.isoformat(sep='T', timespec='auto')
        # 00:00:00
        _time.isoformat(timespec='auto')
        # 2023-02-11
        _date.isoformat()


# 字符串格式化转 date time datetime
def str_to_object():
    def _strptime():
        # 2023-02-11 00:00:01.000001+00:00
        datetime.datetime.strptime("2023-02-11T00:00:01.000001+00:00", "%Y-%m-%dT%H:%M:%S.%f%z")
        # 2023-02-11 00:00:00
        datetime.datetime.strptime("2023-02-11", "%Y-%m-%d")
        # 1900-01-01 00:00:01.000001+00:00
        datetime.datetime.strptime("00:00:01.000001+00:00", "%H:%M:%S.%f%z")

        import time
        # time.struct_time(tm_year=2023, tm_mon=12, tm_mday=2, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=336, tm_isdst=-1)
        time.strptime('02/12/23 00:00:00.000000+00:00', '%d/%m/%y %H:%M:%S.%f%z')

    def _fromisoformat():
        # YYYY-MM-DDT[*HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]]
        datetime.datetime.fromisoformat("2023-02-12 00:00:00.000000+00:00")
        # 2023-02-12 00:00:00+00:00

        # YYYY-MM-DD
        datetime.date.fromisoformat("2023-02-12")
        # 2023-02-12

        # HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]
        datetime.time.fromisoformat("00:00:00.000000+00:00")
        # 00:00:00+00:00


# date time datetime 替换
def object_replace():
    # year, month, day, hour, minute, second, microsecond, tzinfo, fold
    _datetime.replace()
    # year, month, day
    _date.replace()
    # hour, minute, second, microsecond, tzinfo, fold
    _time.replace()


_datetime.max()
_date.max()
_time.max()
_timedelta.max()

_datetime.min()
_date.min()
_time.min()
_timedelta.min()

_datetime.resolution()
_date.resolution()
_time.resolution()
_timedelta.resolution()

# 作用 返回包含日期和时间的字符串
# 参数 此功能不接受任何参数。
# 返回 Sat Feb 11 00:00:00 2023
_datetime.ctime()
_date.ctime()

# datetime.datetime：表示日期时间的类，常用的属性有hour, minute, second, microsecond
_datetime.timetuple()

_datetime.weekday()
_datetime.today()
_datetime.now()
_datetime.date()
_datetime.time()

_datetime.astimezone()
_datetime.combine()
_datetime.dst()

_datetime.fromordinal()
_datetime.fromtimestamp()

_datetime.isocalendar()
_datetime.isoweekday()

_datetime.timestamp()

_datetime.timetz()
_datetime.toordinal()
_datetime.tzname()

_datetime.utcfromtimestamp()
_datetime.utcnow()
_datetime.utcoffset()
_datetime.utctimetuple()


# datetime.date：表示日期的类，常用的属性有year, month, day

_date.timetuple()

_date.today()
_date.weekday()

_date.fromordinal()
_date.fromtimestamp()

_date.isocalendar()
_date.isoweekday()

_date.toordinal()


# datetime.time：表示时间的类
_time.dst()
_time.tzname()
_time.utcoffset()

# datetime.tzinfo：时区的相关信息
_tzinfo.dst()
_tzinfo.fromutc()
_tzinfo.tzname()
_tzinfo.utcoffset()


# datetime.timedelta：表示时间间隔，即两个时间点的间隔。
# 在日期上做天days，小时hour，分钟，秒，毫秒，微妙的时间计算
_timedelta.total_seconds()
