import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test.xlsx'
wb1 = opx.load_workbook(wp1)
ws1 = wb1['Sheet']

for i in range(1,8,2):
    data1 = ws1.cell(row = i, column = 2)
    print(data1.value)
