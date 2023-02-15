#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/02/13
# file: 处理数据转模板.py
# Email:
# Author: rakiwine

from init import *

templateDocument = docx.Document()
dealDocument = docx.Document(dealDocumentPath)
all_paragraphs = dealDocument.paragraphs

# 全文西文字体
templateDocument.styles['Normal'].font.name = 'Calibri'
# 全文西文字体大小
templateDocument.styles['Normal'].font.size = Pt(12)
# 全文中文字体
templateDocument.styles['Normal'].element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体(正文)')

# WD_STYLE_TYPE
# 段落样式（PARAGRAPH）、字符样式（CHARACTER）、表格样式（TABLE）和列表样式（LIST）
redStyle = templateDocument.styles.add_style('redStyle', WD_STYLE_TYPE.PARAGRAPH)
redStyle.font.name = '宋体(正文)'
redStyle.font.size = Pt(12)
redStyle.font.color.rgb = RGBColor(255, 0, 0)
redStyle.element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体(正文)')

# 选项识别 字母开头.非空格选项
optionPattern = re.compile(r"(\w)\.([^ ]*)")
# 问题识别答案
answerPattern = re.compile(r"【(\w+)】")
indexPattern = re.compile(r"^[\d]*?\.")

problemGroupList = []
problemGroup = {}
problemCount = 0
for paragraph in all_paragraphs:
    lineDeal = paragraph.text

    for line in lineDeal.split("\n"):
        if "【" in line and "】" in line:
            problemCount += 1
            if problemCount != 1:
                problemGroupList.append(problemGroup)
            # 答案匹配
            answer = answerPattern.findall(line)
            # 问题答案替换：
            problem = answerPattern.sub("：", line)
            # 问题序号移除
            problem = indexPattern.sub("", problem)
            problemGroup = {"problem": problem, "answer": answer}

            # print(line)
            # print(problem)
            if len(answer) > 1:
                print("Error answer more {}".format(answer))
            # print()
            pass
        else:
            optionList = optionPattern.findall(line)
            # print(line)
            for option in optionList:
                optionDict = {
                    "option": option[0],
                    "describe": option[1],
                }
                if problemGroup.get("optionList"):
                    problemGroup["optionList"].append(optionDict)
                else:
                    problemGroup["optionList"] = [optionDict]
                # print("{}".format(item[1]))
                # print("{}.{}".format(option[0], option[1]))
                pass
            # print()
            pass

for index, problemGroup in enumerate(problemGroupList):
    if problemGroup.get("problem"):

        templateDocument.add_paragraph("{}.{}".format(index + 1, problemGroup["problem"]))
        for optionDict in problemGroup["optionList"]:
            templateDocument.add_paragraph("{}.{}".format(optionDict["option"], optionDict["describe"]))
        templateDocument.add_paragraph("答案：{}".format(problemGroup["answer"][0]))
        templateDocument.add_paragraph("难易程度：", style=redStyle)
        templateDocument.add_paragraph("答案解析：", style=redStyle)
        templateDocument.add_paragraph("题型：", style=redStyle)
        templateDocument.add_paragraph("")

# 文件存在 清空 不存在 创建
templateDocument.save(templateDocumentPath)