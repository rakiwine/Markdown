#!/usr/bin/env python
# encoding: utf-8
# Date: 2022/07/23
# file: 字符串单词计数.py
# Email:
# Author: rakiwine 

from collections import Counter

myStr = 'sdfsfsfsdfsd, were, hrhrgege. sdfwe! sfsdfs'

print(dict(Counter(myStr)))
