#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/02/14
# file: init.py
# Email:
# Author: rakiwine

"""

1234.中文【abcd】
a.非空格 b.非空格
c.非空格
d.非空格

转换

1234.中文：
a.非空格
b.非空格
c.非空格
d.非空格
答案：abcd
难易程度：
答案解析：
题型：

"""

import re
import docx
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt, RGBColor
from docx.oxml.ns import qn

fileName = "妊娠合并心脏病（试题）.docx"
# fileName = "妊娠期糖尿病（试题）.docx"
# fileName = "正常产褥期母儿的护理练习题.docx"
# fileName = "胎儿窘迫及新生儿窒息（试题）.docx"

# D:\Work\Markdown\Life\zhou\试题转模板\data\妊娠合并心脏病（试题）.docx
originalDocumentPath = "D:/Work/Markdown/Life/zhou/试题转模板/data/{}".format(fileName)
# D:\Work\Markdown\Life\zhou\试题转模板\处理 妊娠合并心脏病（试题）.docx
dealDocumentPath = "D:/Work/Markdown/Life/zhou/试题转模板/{} {}".format("处理", fileName)
# D:\Work\Markdown\Life\zhou\试题转模板\模板 妊娠合并心脏病（试题）.docx
templateDocumentPath = "D:/Work/Markdown/Life/zhou/试题转模板/{} {}".format("模板", fileName)
