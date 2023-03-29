import openpyxl as opx

p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\anki_1678953594.xlsx'

wb1 = opx.load_workbook(p+f1)
ws3 = wb1['3号']
ws3['J3'] = "=SUM(A3:F3)"





wb1.save(p+f1)
