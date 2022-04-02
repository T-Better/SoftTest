import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test.xlsx'
wb1 = opx.load_workbook(wp1)
ws1 = wb1['Sheet']
ws1['E1'] = '评价'
warea = ws1.iter_rows(min_row=2,min_col = 2)
for r in warea:
    sg = sum([cel.value for cel in r][:-1])
    if sg >= 270:
        r[-1].value = '优秀'
wb1.save(wp1)
