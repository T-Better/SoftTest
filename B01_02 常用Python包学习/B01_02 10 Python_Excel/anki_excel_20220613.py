import openpyxl as opx

p1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs\{}'.format('test1654591815.xlsx')

path2 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs\fruit_price.xlsx'
wb1 = opx.load_workbook(path2)
ws1 = wb1['第1号']

res_list = []

for row in ws1.iter_rows(min_row=2):
    tmp = []
    for c in row:
        tmp.append(c.value)
    res_list.append(tmp)

print(res_list)







