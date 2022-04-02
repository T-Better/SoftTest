import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test.xlsx'
wb1 = opx.load_workbook(wp1)
ws1 = wb1['Sheet']

# 方法一：
cell1 = ws1['A6'].value
print(cell1)

# 方法二
cell2 = ws1.cell(1,6)
print(cell2.value)

wb1.close()