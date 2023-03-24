import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1637828640.xlsx'
wb1 = opx.load_workbook(wp1)
ws5 = wb1['5号']

# 在最后一行写入数据
ws5.append([1,2,3,4,5])

# 1.获取1-3列，1-5行数据，分别使用按行、按列、区域3种方法法
# 方法一：
for i in ws5['A1:C5']:
    for c in i:
        print(c.value)

# 方法二：
for j in ws5.iter_rows(min_row=1,max_row=5,min_col=1,max_col=3):
    for c in j:
        print(c.value)

# 方法三
for k in ws5.iter_clos(min_row=1, max_row=5, min_col=1,max_col=3):
    for c in k:
        print(c.value)

"""
对工作表中数据实现以下效果：第一行均为双实线对象，
第二行及一下所有内部边框均为单实线黑色
"""
side_header = opx.styles.Side(style='double', color='000000')  # 双实线边框
side_content = opx.styles.Side(style='thin', color='000000')  # 单实线黑色

border_header = opx.styles.Border(top = side_header,bottom = side_header,left = side_header,right = side_header))
border_content = opx.styles.Border(top = side_content,bottom = side_content,left = side_content,right = side_content)

# content
for i in ws5['A2 : J10']:
    for c in i:
        c.border = border_content

for j in ws5['A1:J1']:
    for c in j:
        c.border = border_header

# 设置第一行高30，第一列宽15
ws5.row_dimensions[1].height = 30
ws5.column_dimensions['A'].width = 15

# 1.让标题水平垂直居中且自动换行；2.让正文自动换行
ali_header = opx.styles.Alignment(vertical = 'center', horizontal='center', wrap_text = True)
ali_content = opx.styles.Alignment(warp_text = True)

for i in ws5['A1:J1']:
    for c in i:
        c.alignment = ali_header

for j in ws5['A2:J10']:
    for c in j:
        c.alignment = ali_content

# 在某个excel的第一个sheet页第五列后面删除1列
ws5.delete_cols('E1',1)

wb1.save(wp1)