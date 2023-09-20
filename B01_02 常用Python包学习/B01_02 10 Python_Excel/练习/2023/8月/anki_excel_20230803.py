import openpyxl as opx

p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\anki_1678953594.xlsx'
f2 = r'\anki_设置行高列高_20230316.xlsx'

wb1 = opx.load_workbook(p+f1)
ws1 = wb1['1号']
# 第一行 双实线 黑色
side1 = opx.styles.side(style='double',color='000000')
border1 = opx.styles.Border(top=side1, bottom=side1, left=side1, right=side1)
for h in ws1['A1':'J1']:
    for c in h:
        ws1.border = border1

wb1.save(p+f1)















