import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1637828640.xlsx'

wb1 = opx.load_workbook(wp1)
ws1 = wb1['1号']

pf_header = opx.styles.PatternFill(fill_type = 'solid',
                    start_color='FFFFFF',end_color='000000')

for i in ws1['A1:J1']:
    for c in i:
        c.fill = pf_header

wb1.save(wp1)
