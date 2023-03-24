import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test.xlsx'
wb1 = opx.load_workbook(wp1)
ws1 = wb1['Sheet']

rs = ws1.rows
for i in rs:
    for j in i:
        print(j.value)

cs = ws1.columns
for i in cs:
    for j in i:
        print(j.value)
wb1.close()