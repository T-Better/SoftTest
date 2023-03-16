import openpyxl as opx


p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\anki_1678953594.xlsx'
f2 = r'\anki_设置行高列高_20230316.xlsx'

wb1 = opx.load_workbook(p+f1)
ws1 = wb1['1号']
# 第一行 双实线 黑色
line1 = opx.styles.Side(style='double', color='000000')
border1 = opx.styles.Border(left=line1,right=line1,top=line1,bottom=line1)
for h in ws1['A1':'J1']:
    for c in h:
        c.border = border1

# 后面几行
line2 = opx.styles.Side(style='thin', color = '000000')
border2 = opx.styles.Border(left=line2,right=line2,top=line2,bottom=line2)
for t in ws1['A2':'J10']:
    for c in t:
        c.border = border2

wb1.save(p+f1)
