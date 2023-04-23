import openpyxl as opx
wpf = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\刘子君 成方金信工作量表.xlsx'
wb1 = opx.load_workbook(wpf)
ws1 = wb1['5月']

# 向一个区域内写入数据
ws1['A1'].value = '张三'


"""
*读取工作表S1的最大行、列；
A1单元格的值（两种方法）
*A1单元格的行、列位置
"""
wmr = ws1.max_rows

wmc = ws1.max_column()

c1 = ws1['A1'].column
r1 = ws1['A1'].row

# 将模板批量复制 将Sheet1复制31份，然后删除Sheet1模板
wsi = wb1.copy_worksheet(wb1['sheet1'])
wsi.title = '1号'
wb1.remove(wb1['Sheet'])

wb1.save()
