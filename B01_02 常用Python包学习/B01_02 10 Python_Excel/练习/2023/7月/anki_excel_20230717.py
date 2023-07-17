
import openpyxl as opx

p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\anki_1678953594.xlsx'
f2 = r'\anki_设置行高列高_20230316.xlsx'

wb1 = opx.load_workbook(p + f1)
ws2 = wb1['2号']
# 微软雅黑 11号 红色 加粗 倾斜 单下划线
fh = opx.styles.Font(name='微软雅黑', size=11,color='FF0000', bold=True, italic=True, under_line='thin')
for r in ws2['A2:J2']:
    for c in r:
        c.alignment = fh

wb1.save( p +f1)














