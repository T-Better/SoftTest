import openpyxl as opx

path1 = r'D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_03 自动化办公\C06_03 02 Excel_Python\002 Docs\test1644204065.xlsx'
wb1 = opx.load_workbook(path1)
ws1 = wb1['1号']

# 对工作表中数据实现以下效果：第一行均为双实线对象，第二行及一下所有内部边框均为单实线黑色
side_header = opx.styles.Side(style='double')
side_context = opx.styles.Side(style = 'thin')

border_header = opx.styles.Border(top=side_header,bottom=side_header, \
                                  left=side_header,right=side_header)
border_context = opx.styles.Border(top=side_context,bottom=side_context, \
                                   left=side_context,right=side_context)
for r in ws1['A1:J1']:
    for c in r:
        c.border = border_header

for j in ws1['A2:J10']:
    for c in j:
        c.border = border_context

wb1.save(wb1)

