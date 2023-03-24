import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1637753231.xlsx'

wb1 = opx.load_workbook(wp1)
ws8 = wb1['8号']

ali1 = opx.styles.Alignment(horizontal = 'center',vertical = 'center',wrap_text = True)
for i in ws8['A1:J1']:
    for c in i:
        c.alignment = ali1

ali2 = opx.styles.Alignment(horizontal = 'general',vertical='center',wrap_text = True)
for j in ws8['A2:J10']:
    for c in j:
        c.alignment = ali2

wb1.save(wp1)
