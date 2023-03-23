"""
1.让标题水平垂直居中且自动换行
2.让正文自动换行
"""
import openpyxl as opx

p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\anki_1678953594.xlsx'
f2 = r'\anki_设置行高列高_20230316.xlsx'

wb1 = opx.load_workbook(p+f1)
ws1 = wb1['1号']

# 标题水平垂直居中且自动换行
# TODO 这里写
for h in ws1['A1':"J1"]:
    for c in h:
        pass # TODO 这里写

# 正文水平居中且自动换行
# TODO 这里写
for t in ws1['A2':'J10']:
    for c in t:
        pass # TODO 这里写

wb1.save(p+f1)



