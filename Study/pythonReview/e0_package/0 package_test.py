#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/01/30
# file: 0 package_test.py
# Email:
# Author: rakiwine

# 导入 Phone 包
from importlib import reload

import package_runoob

from package_runoob import runoob1
from package_runoob import runoob2

key = None
ces = None

for key, ces in locals().items():
    # print(key, ces)
    pass

runoob1.runoob1()
reload(package_runoob)
runoob2.runoob2()
