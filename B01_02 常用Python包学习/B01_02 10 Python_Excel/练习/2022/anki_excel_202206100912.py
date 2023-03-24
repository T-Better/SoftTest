import openpyxl as opx

p1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs\{}'.format('test1654591815.xlsx')
wb1 = opx.load_workbook(p1)
ws1 = wb1['第1号']

# 在某个excel的第一个sheet页第五列后面删除1列
ws1.delete_cols(5,1)




