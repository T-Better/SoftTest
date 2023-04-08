import openpyxl as opx

p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\anki_1678953594.xlsx'
f2 = r'\anki_设置行高列高_20230316.xlsx'

wb1 = opx.load_workbook(p + f1)
ws2 = wb1['2号']
# 获取test.xlsx第一个工作表名称并将其重命名为1月
ws2.title = '1月'

# 获取第2列1、3、5、7行的数据
for n in range(1,8,2):
    print(ws2.cell(row = n,column = 2).value)

wb1.save(p+f1)

