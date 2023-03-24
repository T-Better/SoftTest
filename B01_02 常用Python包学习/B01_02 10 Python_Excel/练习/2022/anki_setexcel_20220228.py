import openpyxl as opx

path1 = r'D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_03 自动化办公\C06_03 02 Excel_Python\002 Docs\test1644204065.xlsx'
wb1 = opx.load_workbook(path1)
ws4 = wb1['4号']

# 标题加粗 22号 微软雅黑；正文：宋体 11号；重点：红色加粗倾斜单下划线11号字体
font_header = opx.styles.Font(name='微软雅黑',bold=True, size=22,color='000000')
font_text = opx.styles.Font(name='宋体', size=11,color='000000')
font_special = opx.styles.Font(bold=True, size=11, color='FF0000',italic=True, underline='single')

for row in ws4['A1:J1']:
    for c in row:
        c.font = font_header

for i in ws4['A2:J12']:
    for c in i:
        c.font = font_text

for j in ws4['A5:J5']:
    for c in j:
        c.font = font_special

wb1.save(path1)


