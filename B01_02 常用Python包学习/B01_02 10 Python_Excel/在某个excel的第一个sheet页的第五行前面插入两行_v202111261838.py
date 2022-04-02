import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1637828640.xlsx'

wb1 = opx.load_workbook(wp1)
# ws2 = wb1['2号']

# ws2.insert_rows(5,2)
# ws2.row_dimensions[1].height = 40
# ws2.column_dimensions['A'].width = 15
ws3 = wb1['3号']
# ws1.title = '1月'

# 1.定义线
side_thin = opx.styles.Side(style = 'thin',color = '000000')
side_double = opx.styles.Side(style = 'double',color='000000')

# 2.定义单元格边框
border_thin = opx.styles.Border(left=side_thin,right=side_thin,top=side_thin,bottom=side_thin)
border_double = opx.styles.Border(left=side_double,right=side_double,top=side_double,bottom=side_double)

# 3. 对表格操作
# 3.1 先画细线
for i in ws3['A1:J10']: 
    for c in i:
        c.border = border_thin

for j in ws3['A1:J1']:
    for c in j:
        c.border = border_double

# 设置第一行高30，第一列宽15
ws3.row_dimensions[1].height = 30
ws3.column_dimensions['A'].wight = 15

wb1.save(wp1)
