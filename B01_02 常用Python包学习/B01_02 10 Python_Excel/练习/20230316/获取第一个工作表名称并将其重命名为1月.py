import openpyxl as opx

fp = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs\anki_1678953594.xlsx'

wb1 = opx.load_workbook(fp)
wss = wb1.worksheets

# 获取工作表名称并将其重命名为2月
print(wss[2].title)
wss[2].title = '2月'

wb1.save(fp)



