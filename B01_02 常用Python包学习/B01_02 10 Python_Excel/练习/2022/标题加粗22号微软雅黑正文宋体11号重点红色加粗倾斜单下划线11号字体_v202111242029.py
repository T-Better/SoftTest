import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1637753231.xlsx'

wb1 = opx.load_workbook(wp1)
ws7 = wb1['7号']

font1 = opx.styles.Font(name=u'微软雅黑',size=22,bold=True)
for i in ws7['A1:J1']:
    for c in i:
        c.font = font1

font2 = opx.styles.Font(name=u'宋体',size=11)
for j in ws7['A2:J10']:
    for c in j:
        c.font = font2

font3 = opx.styles.Font(name=u'宋体',size=11, color='FF0000',underline = 'single',bold = True,italic = True)
for k in ws7['A3:J3']:
    for c in k:
        c.font = font3
wb1.save(wp1)
