#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/02/11
# file: _datetime.py
# Email:
# Author: rakiwine

# epoch	时间开始的点，取决于平台
# UTC	协调世界时（Coordinated Universal Time），格林威治标准时间（GMT）
# DST	夏令时（Daylight Saving Time）

from pytz import utc, timezone
import datetime
from datetime import timezone as _timezone

# 猜测第三方插件原理 返回时区子类
de = timezone('Europe/Berlin')
cn = timezone('Asia/Shanghai')

beijing = _timezone(datetime.timedelta(hours=8))

ts = datetime.datetime.now().timestamp()
# 0001 <= year <= 9999
# 1 <= month <= 12
# 1 <= day <= 给定年月对应的天数
# 0 <= hour < 24
# 0 <= minute < 60
# 0 <= second < 60
# 0 <= microsecond <1000,000
# tzinfo 默认None tzinfo 子类的实例
# fold in [0, 1] 默认0 文档无描述
_datetime = datetime.datetime(year=2023, month=2, day=11, hour=0, minute=0, second=0, microsecond=0, tzinfo=cn)

_date = datetime.date(year=2023, month=2, day=11)
# _date.year, _date.month, _date.day

_time = datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=utc)
# _time.hour, _time.minute, _time.second, _time.microsecond, _time.tzinfo, _time.fold

_tzinfo = datetime.tzinfo()

# 999999999 days -999999999 九亿
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
        # 时间元组
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


# 对象所能表示的最大日期
# 9999-12-31 23:59:59.999999
datetime.datetime.max
# 9999-12-31
datetime.date.max
# 23:59:59.999999
datetime.time.max
# 999999999 days, 23:59:59.999999
datetime.timedelta.max

# 对象所能表示的最小日期
# 0001-01-01 00:00:00
datetime.datetime.min
# 0001-01-01
datetime.date.min
# 00:00:00
datetime.time.min
# -999999999 days, 0:00:00
datetime.timedelta.min

# 表示日期的最小单位
# 0:00:00.000001
_datetime.resolution
# 1 day, 0:00:00
_date.resolution
# 0:00:00.000001
_time.resolution
# 0:00:00.000001
_timedelta.resolution

# 作用 返回包含日期和时间的字符串
# 参数 此功能不接受任何参数
# 返回 str类型 Sat Feb 11 00:00:00 2023
_datetime.ctime()
_date.ctime()


"""
0	tm_year	（例如，1993）
1	tm_mon	range [1, 12]
2	tm_mday	range [1, 31]
3	tm_hour	range [0, 23]
4	tm_min	range [0, 59]
5	tm_sec	range [0, 61]
6	tm_wday	range [0, 6] ，周一为 0
7	tm_yday	range [1, 366]
8	tm_isdst	0, 1 或 -1；
tm_isdst 可以在夏令时生效时设置为1，而在夏令时不生效时设置为0
值-1表示这是未知的，并且通常会导致填写正确的状态
"""
# 作用 返回 [UTC]时间元组
# 参数 此功能不接受任何参数
# 返回 time.struct_time类型 time.struct_time(tm_year=2023, tm_mon=2, tm_mday=11, tm_hour=0, tm_min=0, tm_sec=1, tm_wday=5, tm_yday=42, tm_isdst=0)
_datetime.utctimetuple()
_datetime.timetuple()
_date.timetuple()

"""
weekday    isoweekday
0	       1            Monday
1	       2            Tuesday
2	       3            Wednesday
3	       4            Thursday
4	       5            Friday
5	       6            Saturday
6	       7            Sunday
"""
# 作用 根据给定的 DateTime 获取周数
# 参数 此功能不接受任何参数
# 返回 int [0123456]
_datetime.weekday()
_date.weekday()
# 返回 int [1234567]
_datetime.isoweekday()
_date.isoweekday()

# 作用 获取当前设备今天日期
# 参数 此功能不接受任何参数
# 返回 datetime.datetime类型 2023-02-13 14:58:57.009273
datetime.datetime.today()
datetime.date.today()

# 作用 一种日历表示方法，类似于我国的农历，西方国家使用比较多，此处不详细展开讨论
# 参数
# 返回
# _datetime.fromordinal()
# _date.fromordinal()

# 作用 获取本地时间
# 参数 时间戳 datetime.datetime.now().timestamp()
# 返回 datetime.datetime类型 2023-02-13 15:04:13.533700 utc -8h
datetime.datetime.utcfromtimestamp(ts)
datetime.datetime.fromtimestamp(ts)
datetime.date.fromtimestamp(ts)

# 作用 返回格式如(year，month，day)的元组
# 参数
# 返回 tuple (2023, 6, 6) 不包含时间
_datetime.isocalendar()
_date.isocalendar()

# 作用 返回公元公历开始到现在的天数公元1年1月1日为1
# 参数 此功能不接受任何参数
# 返回 int 738563
_datetime.toordinal()
_date.toordinal()

# 作用 tzinfo=None 返回 None
# 参数 此功能不接受任何参数
# 返回 None | datetime.timedelta类型 0:00:00
_datetime.dst()
_time.dst()
# _tzinfo.dst(_datetime) 子类未实现 dst

# 作用 以字符串形式返回传递的 DateTime 对象的时区名称
# 参数 此功能不接受任何参数
# 返回 字符串 LMT UTC
_datetime.tzname()
_time.tzname()
# _tzinfo.tzname(_datetime) 子类未实现 tzname


# 作用 返回与给定实例中指定的tzinfo的 UTC偏移量对应的timedelta实例
# 参数 此功能不接受任何参数
# 返回 datetime.timedelta类型 偏移量
_datetime.utcoffset()
_time.utcoffset()
# _tzinfo.utcoffset(_datetime) 子类未实现 utcoffset

# datetime.datetime：表示日期时间的类
# 2023-02-13 08:41:25.698475
_datetime.utcnow()
# 2023-02-13 16:41:37.691550
_datetime.now()
# 2023-02-12
_datetime.date()
# 00:00:01.000001
_datetime.time()

# 作用 修改日期时间为对应时区
# 参数 timezone
# 返回 默认无参8h时区 2023-02-11 23:54:01.000001+08:00
_datetime.astimezone()


# 作用 把指定的date和time对象整合为datetime对象
# 参数 _date, _time
# 返回 datetime.timedelta类型
_datetime.combine(_date, _time)

# 作用 返回时间戳
# 参数 此功能不接受任何参数
# 返回 float类型
_datetime.timestamp()

# 作用 返回日期时间相同的时间时区部分
# 参数 此功能不接受任何参数
# 返回 datetime.time类型
_datetime.timetz()

# datetime.date：表示日期的类

# datetime.time：表示时间的类

# datetime.tzinfo：时区的相关信息

# 作用 此函数使用UTC占用对象的日期和时间，并返回等效的本地时间。
# 它主要用于调整日期和时间
# _tzinfo.fromutc()

# datetime.timedelta：表示时间间隔，即两个时间点的间隔
# 在日期上做天days，小时hour，分钟，秒，毫秒，微妙的时间计算

# 使用seconds时，如果时间差为负数，会变成86399+(时间差)
# 导致计算错误。原因：seconds只计算时间差，没包含日期，
# 一天的秒数为24*60*60=86400，seconds范围为[0, 86399]
# 作用 返回日期时间相差的秒数
# 参数
# 返回 float类型
_timedelta.total_seconds()

# 作用 返回日期时间相差的秒数
# 参数
# 返回 float类型
(_datetime - _datetime).total_seconds()
