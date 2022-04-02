import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test.xlsx'

wb1 = opx.load_workbook(wp1)
ws1 = wb1['Sheet']
for r in ws1.iter_rows(min_row=2,min_col=2):
    for cel in r:
        if cel.value == None:
            cel.value = '缺考'

wb1.save(wp1)