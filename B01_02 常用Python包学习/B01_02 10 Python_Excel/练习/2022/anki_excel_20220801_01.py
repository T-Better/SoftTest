import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1654591815.xlsx'

wb1 = opx.load_workbook(wp1)
ws2 = wb1['第2号']

ali1 = opx.styles.Alignment(horizontal='center',vertical='center',wrap_text=True)
ali2 = opx.styles.Alignment(wrap_text=True)
for i in ws2['A1:Z1']:
    for c in i:
        c.alignment=ali1

for j in ws2['A2:Z10']:
    for c in j:
        c.alignment=ali2

wb1.save(wp1)



















