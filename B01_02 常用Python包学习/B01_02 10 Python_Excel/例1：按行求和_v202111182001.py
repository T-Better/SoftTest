import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test.xlsx'

wb1 = opx.load_workbook(wp1)
ws1 = wb1['Sheet']
for r in list(ws1.rows)[1:]:
    data = [cel.value for cel in r if type(cel.value)==int]
    print(data[0],sum(data[1:]))
