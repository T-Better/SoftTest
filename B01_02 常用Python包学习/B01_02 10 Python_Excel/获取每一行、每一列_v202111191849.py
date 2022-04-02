import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test.xlsx'

wb1 = opx.load_workbook(wp1)
ws1 = wb1['Sheet']

# 获取每一行
for r in ws1.rows:
    for i in r:
        print(i.value, end=" ")

# 获取每一列
for c in ws1.columns:
    for i in c:
        print(i.value, end="|")

wb1.close()