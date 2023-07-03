import openpyxl as opx

p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\anki_1678953594.xlsx'
f2 = r'\anki_设置行高列高_20230316.xlsx'

wb1 = opx.load_workbook(p+f1)
ws1 = wb1['1号']
# 第一行 双实线 黑色
s1 = opx.styles.Side(color='000000',style='double')
b1 = opx.styles.Border(top=s1,bottom=s1,left=s1,right=s1)
for h in ws1['A1':'J1']:
    for c in h:
        c.border = b1



wb1.save(p+f1)


