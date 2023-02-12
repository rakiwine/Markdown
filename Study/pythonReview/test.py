#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/02/06
# file: test.py
# Email:
# Author: rakiwine

import time
import datetime


_date = datetime.date(year=2023, month=2, day=11)
_time = datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
_tzinfo = datetime.tzinfo()
_datetime = datetime.datetime(year=2023, month=2, day=11, hour=0, minute=0, second=1, microsecond=1, tzinfo=None)
_timedelta = datetime.timedelta(weeks=1, days=1, hours=1, minutes=1, seconds=1, milliseconds=1, microseconds=1)


# {[name][:][[fill]
# align][sign][  # ][0][width][,][.precision][type]}
#     align < >  ^
# sign +-表示左对齐
# 0
# 0
# 填充
#
# 数字格式化
#
# {: .2f} // 保留小数点后两位
# {: +.2f} // 带 + -号保留
# {:.2f}补空格
# {: .0f} // 不带小数
# {: 0 > 2d} // 不足两位左边补0
# {: > 10d}补空格
# {: x < 4d} // 不足四位右边补x
# {: < 10d}补空格
# {: * ^ 10d} // 居中补 *
# {: ^ 10d}补空格
# {:, } // 每三位分隔
# {: .2 %} // 保留两位的百分数形式
# {: .2e} // 指数计数法(科学计数法)
#
# {: b} // 二进制
# {:  # b}0b
# {:d} // 十进制 == {:  # d}
# {:o} // 八进制
# {:  # o}0o
# {:x} // 十六进制
# {:  # x}0x{:#X}0X
