import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1637828640.xlsx'

wb1 = opx.load_workbook(wp1)
ws1 = wb1['1号']

# font_header = opx.styles.Font(bold=True, name=u'微软雅黑',size=22)
# for i in ws1['A1:J1']:
#     for c in i:
#         c.font = font_header

# font_content = opx.styles.Font(name=u'宋体',size=11)
# for j in ws1['A2:J11']:
#     for c in j:
#         c.font = font_content

# font_special = opx.styles.Font(color='FF0000',bold=True,underline = 'single',italic = True)
# for k in ws1['A5:J5']:
#     for c in k:
#         c.font = font_special

note1 = opx.comments.Comment('已完成','辣子鸡')
ws1['A1'].comment = note1

wb1.save(wp1)