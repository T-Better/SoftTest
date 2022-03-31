# anki_复习_20220118.py
import openpyxl as opx

path1 = ''
wb1 = opx.load_workbook(path1)
ws1 = wb1['1月']

# 对工作表中数据实现以下效果：第一行均为双实线对象，第二行及一下所有内部边框均为单实线黑色
side_header = opx.styles.Side(style='double',color='000000')
side_content = opx.styles.Side(style='thin',color='000000')

border_header = opx.styles.Border(left=side_header,right=side_header,top=side_header,bottom=side_header)
border_content = opx.styles.Border(left=side_content,right=side_content,top=side_content,bottom=side_content)

for i in ws1['A1:J1']:
    for c in i:
        c.border = border_header

for j in ws1['A2:J11']:
    for c in j:
        c.border = border_content

wb1.save(path1)