import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1640048977.xlsx'
wb1 = opx.load_workbook(wp1)
ws2 = wb1['2号']

# ws2.move_range('A1:C3',rows=2,columns=1)

"""
1.获取1-3列，1-5行数据，分别使用按行、按列、区域3种方法法
"""
# 方法一：
for i in ws2['A1:C5']:
    for c in i:
        print(c.value)

# 方法二：
for i in ws2.iter_rows(min_row=1,max_row=5,min_col=1,max_col=3):
    for c in i:
        print(c.value)

# 方法三
for j in ws2.iter_columns(min_row=1,max_row=5,min_col=1,max_col=3):
    for c in j:
        print(c.value)
        
wb1.save(wp1)

ws2.move_range("A1:C3",rows=2,columns=1)
