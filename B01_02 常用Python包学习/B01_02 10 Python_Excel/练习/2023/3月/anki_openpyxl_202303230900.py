import openpyxl as opx


p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\anki_1678953594.xlsx'
f2 = r'\anki_设置行高列高_20230316.xlsx'

wb1 = opx.load_workbook(p+f1)
ws1 = wb1['1号']
"""
# 第一行 双实线 黑色
s1 = opx.styles.Side(style='double',color='000000')
b1 = opx.styles.Border(left=s1, right=s1, top=s1, bottom=s1)
for h in ws1['A1':'J1']:
    for c in h:
        c.border = b1

# 后面几行
s2 = opx.styles.Side(style='thin', color='000000')
b2 = opx.styles.Border(left=s2, right=s2,top = s2, bottom = s2)
for t in ws1['A2':'J10']:
    for c in t:
        c.border = b2
"""

# 给一下目录中的某个excel单元格A1做“已完成”批注
n1 = opx.comments.Comment('已完成', 'chase')
ws1['J1'].comment = n1

wb1.save(p+f1)





