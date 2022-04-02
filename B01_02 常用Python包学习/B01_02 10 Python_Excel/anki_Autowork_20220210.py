import openpyxl as opx

path1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\002 Docs\test1644204065.xlsx'
wb1 = opx.load_work(path1)
ws3 = wb1['3号']

# 设置第一行高30，第一列宽15
ws3.row_dimensions[1].height = 30
ws3.column_dimensions['A'].width = 15

# 在某个excel的第一个sheet页的第五行前面插入两行
ws3.insert_rows[5, 2]

# 1.用两种方法获取一个单元格的值
# 方法1：
ws3['A1'].value

# 方法2：
ws3.cell(row=1,cloumns=1).value

wb1.save(path1)
