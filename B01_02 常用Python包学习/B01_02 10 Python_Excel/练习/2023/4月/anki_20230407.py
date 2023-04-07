import openpyxl as opx

p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\anki_1678953594.xlsx'
wb1 = opx.load_workbook(p+f1)
ws4 = wb1['4号']


# 在最后一行写入数据
ws4.append(['c','d'])


wb1.save(p+f1)
