import openpyxl as opx

wpf = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\刘子君 成方金信工作量表.xlsx'
wb1 = opx.load_workbook(wpf)
ws1 = wb1['5月']

# 获取每一行
for r in ws1.rows:
    for c in r:
        print(c.value)
        
# 获取每一列
for l in ws1.columns:
    for c in l:
        print(c.value)