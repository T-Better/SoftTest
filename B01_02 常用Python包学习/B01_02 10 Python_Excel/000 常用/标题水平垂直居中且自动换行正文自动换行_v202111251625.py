import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1637828640.xlsx'

wb1 = opx.load_workbook(wp1)
ws1 = wb1['1号']
# 标题
ali_header = opx.styles.Alignment(horizontal='center',vertical='center',wrap_text = True)
for i in ws1['A1:J1']:
    for c in i:
        c.alignment = ali_header
# 正文
ali_content = opx.styles.Alignment(vertical='center',wrap_text=True)
for j in ws1['A2:J10']:
    for c in j:
        c.alignment = ali_content

wb1.save(wp1)
