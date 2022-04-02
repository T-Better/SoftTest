import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1637828640.xlsx'

wb1 = opx.load_workbook(wp1)
ws2 = wb1['2号']

# 1.创建素材线
side_double = opx.styles.Side(style='double',color = '000000')  # 双实线
side_single = opx.styles.Side(style='thin',color='000000')  # 单实线

# 2.由线组单元格
border_double = opx.styles.Border(left=side_double,right=side_double,top=side_double,bottom=side_double)
border_single = opx.styles.Border(left=side_single,right=side_single,top=side_single,bottom=side_single)

# 3.开始画边框
# 3.1 全部为单实线
for i in ws2['A1:J11']:
    for c in i:
        c.border = border_single

# 3.2 第一行全部为双实线
for j in ws2['A1:J1']:
    for c in j:
        c.border = border_double

wb1.save(wp1)

