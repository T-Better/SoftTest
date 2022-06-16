import openpyxl as opx

p1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs\{}'.format('test1654591815.xlsx')
wb1 = opx.load_workbook(p1)
ws1 = wb1['第1号']

# 用两种方法获取一个单元格的值
# 方法一
i_1 = ws1['A1']
print(i_1.value)

# 方法二
c_1 = ws1.cell(row=1,column=1)
print(c_1.value)

wb1.close()
