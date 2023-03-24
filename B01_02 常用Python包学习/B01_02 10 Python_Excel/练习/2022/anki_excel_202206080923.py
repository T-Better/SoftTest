import openpyxl as opx

p1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs\{}'.format('test1654591815.xlsx')

# 批量修改工作表的名称 将新建100张工作表01.xlsx中第1-100天工作表名改为1-100月
wb1 = opx.load_workbook(p1)
wss = wb1.worksheets
for sheet in wss:
    sheet.title = '第' + sheet.title

wb1.save(p1)



