#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/02/14
# file: 数据源检查处理.py
# Email:
# Author: rakiwine

from init import *

dealDocument = docx.Document()
originalDocument = docx.Document(originalDocumentPath)
all_paragraphs = originalDocument.paragraphs

# 全文西文字体
dealDocument.styles['Normal'].font.name = 'Calibri'
# 全文西文字体大小
dealDocument.styles['Normal'].font.size = Pt(12)
# 全文中文字体
dealDocument.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体(正文)')

# 锁定识别选项
symbolPattern = re.compile(r"([ABCDEFGHI][.．])")
# 字符映射
translate = str.maketrans('／“”（）＜＞℅：；,．', '/""()<>%:;，.')

for paragraph in all_paragraphs:
    lineDeal = paragraph.text

    for line in lineDeal.split("\n"):
        # 处理每行
        dealLine = line.translate(translate)
        # 处理每行所有包含控制符 \x00-\x1f
        # 处理每行所有包含删除   \x7f     del
        # 处理每行所有包含空格   \x20    半角空格
        dealSpaceLine = dealLine.replace(" ", "")
        # 处理每行所有包含 NBSP \xC2\xA0 无间断空间(U 00A0)
        dealSpaceLine = dealSpaceLine.replace(" ", "")
        # 处理每行所有包含      \xE3\x80\x80 双字节空间(U 3000)
        dealSpaceLine = dealSpaceLine.replace("　", "")

        # 增加选项前空格
        addSpaceLine = symbolPattern.sub(" \\1", dealSpaceLine)
        # 处理每行前后空格
        removeSpaceLine = addSpaceLine.strip(" ")

        if len(removeSpaceLine):
            if "【" in line and "】" in removeSpaceLine:
                dealDocument.add_paragraph(removeSpaceLine)
                pass
            else:
                dealDocument.add_paragraph(removeSpaceLine)
                pass

# 文件存在 清空 不存在 创建
dealDocument.save(dealDocumentPath)