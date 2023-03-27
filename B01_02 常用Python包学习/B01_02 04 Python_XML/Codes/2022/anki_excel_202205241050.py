import openpyxl as opx

p1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs\test1653298329.xlsx'
wb1 = opx.load_workbook(p1)
ws1 = wb1['9号']

# 设置第一行高30，第一列宽15
ws1.row_dimensions[1].height = 40
ws1.column_dimensions['A'].width = 15

wb1.save(p1)


