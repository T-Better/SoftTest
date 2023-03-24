import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1637753231.xlsx'

wb1 = opx.load_workbook(wp1)
ws5 = wb1['5号']

font_header = opx.styles.Font(name=u'微软雅黑', bold=True, size=22)
for i in ws5['A1:J1']:
    for c in i:
        c.font = font_header

font_content = opx.styles.Font(name=u'宋体', size=11)
for j in ws5['A2:J10']:
    for c in j:
        c.font = font_content

font_special = opx.styles.Font(name=u'宋体',size=11,color='FF0000',bold=True,underline = 'single',italic=True)
for k in ws5['A4:J4']:
    for c in k:
        c.font = font_special

wb1.save(wp1)

