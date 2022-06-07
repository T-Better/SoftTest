"""
实现功能：标题加粗 22号 微软雅黑；正文：宋体 11号；重点：红色加粗倾斜单下划线11号字体
"""
import openpyxl as opx
p1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs\{}'.format('test1654591815.xlsx')

wb1 = opx.load_workbook(p1)
ws1 = wb1['1号']

font_header = opx.styles.Font(name=u'微软雅黑', bold=True, size=22)
font_content = opx.styles.Font(name=u'宋体', size=11)
font_special = opx.styles.Font(bold=True,underline='single',italic=True,color='FF0000')

for i in ws1['A1':'J1']:
    for c in i:
        c.font = font_header

for j in ws1['A2':'J10']:
    for c in j:
        c.font = font_content

for k in ws1['A5':'J5']:
    for c in k:
        c.font = font_special

# 冻结excel的第一行
ws1.freeze_panes = 'A2'

wb1.save(p1)


