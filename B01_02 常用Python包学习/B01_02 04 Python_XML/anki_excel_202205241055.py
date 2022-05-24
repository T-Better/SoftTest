import openpyxl as opx

p1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs\test1653298329.xlsx'
wb1 = opx.load_workbook(p1)

for i in range(1,32):
    wsi = wb1.copy_worksheet(wb1['9号'])
    wsi.title = str(i)+'日'

wb1.remove(wb1['9号'])
wb1.save(p1)