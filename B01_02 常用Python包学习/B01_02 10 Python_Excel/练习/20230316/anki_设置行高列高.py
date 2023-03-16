import openpyxl as opx


p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\anki_1678953594.xlsx'
f2 = r'\anki_设置行高列高_20230316.xlsx'

wb1 = opx.load_workbook(p+f1)
ws1 = wb1['1号']

# 设置第一行高30
ws1.row_dimensions['1'].height = 30

# 第一列宽15
ws1.column_dimensions['A'].width = 15

wb1.save(p+f2)
