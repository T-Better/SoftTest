import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test.xlsx'

wb1 = opx.load_workbook(wp1)
ws1 = wb1['Sheet']
for rn in range(ws1.max_row,1,-1):
    aso = sum([cel.value for cel in ws1[rn][1:]])
    if aso <= 270:
        ws1.delete_rows(rn)
wb1.save(wp1)