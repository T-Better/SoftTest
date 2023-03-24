import openpyxl as opx

e1 = r'D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_03 自动化办公\C06_03 02 Excel_Python\002 Docs\test1644204065.xlsx'

wb1 = opx.load_workbook(e1)
ws1 = wb1['1号']
# 第一行均为双实线对象，第二行及一下所有内部边框均为单实线黑色
side_head = opx.styles.Side(style='double', color = '000000')
side_content = opx.styles.Side(style='thin', color = '000000')

border_head = opx.styles.Border(left=side_head,right=side_head,top=side_head,bottom=side_head)
border_content = opx.styles.Border(left=side_content,right=side_content,top=side_content,bottom=side_content)

for i in ws1['A2:J10']:
    for c in i:
        c.border = border_content

for j in ws1['A1:J10']:
    for c in j:
        c.border = border_head

wb1.save(e1)



