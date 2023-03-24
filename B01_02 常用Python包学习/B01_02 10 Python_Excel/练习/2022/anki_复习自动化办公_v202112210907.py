import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1640048977.xlsx'
wb1 = opx.load_workbook(wp1)
ws2 = wb1['2号']

# 向一个区域内写入数据
for i in ws2['A1:C1']:
    for c in i:
        c.value = '标题1'

# 对工作表中数据实现以下效果：第一行均为双实线对象，第二行及一下所有内部边框均为单实线黑色
side_header = opx.styles.Side(style='double',color='000000')
side_content = opx.styles.Side(style='thin',color='000000')

border_header = opx.styles.Border(top=side_header,bottom=side_header,left=side_header,right=side_header)
border_content = opx.styles.Border(top=side_header,bottom=side_header,left=side_header,right=side_header)
# 单边框
for i in ws2['A2:J10']:
    for c in i:
        c.border = border_content

# 标题：双边框
for j in ws2['A1:J1']:
    for c in j:
        c.border = border_header

# 设置第一行高30，第一列宽15
ws2.row_dimensions[1].height = 40
ws2.column_dimensions['A'].width = 15

"""
1.用两种方法获取一个单元格的值
print(ws2['A1'].value)
print(ws2.cell(row=1,column='A').value)
"""

# 在某个excel的第一个sheet页的第五行前面插入两行
# ws2.insert_rows(5,2)

# 让标题水平垂直居中且自动换行;让正文自动换行
ali_header = opx.styles.Alignment(horizontal='center',vertical='center',wrap_text=True)
ali_content = opx.styles.Alignment(horizontal = 'center', wrap_text=True)

for i in ws2['A1:J1']:
    for c in i:
        c.alignment = ali_header

for j in ws2['A2:J10']:
    for c in j:
        c.alignment = ali_content

# 给单元格A1做“已完成”批注
note1 = opx.comments.Comment('已完成','lzj')
ws2['A1'].comment = note1

wb1.save(wp1)