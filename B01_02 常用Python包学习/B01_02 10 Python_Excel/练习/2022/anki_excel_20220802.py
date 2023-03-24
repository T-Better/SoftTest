import openpyxl as opx

p1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs\{}'.format('test1654591815.xlsx')

wb1 = opx.load_workbook(p1)
ws3 = wb1['第3号']

for i in range(31):
    wsi=wb1.copy_worksheet(ws3)
    wsi.title='7月'+str(i)+'日'
wb1.remove(ws3)

wb1.save(p1)





