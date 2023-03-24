import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test202111231100.xlsx'

wb1 = opx.load_workbook(wp1)
ws1 = wb1['1月']

# 对A-D列进行分组
# ws1.column_dimensions.group('A','D',hidden=True)

# 对1-5行进行分组
ws1.row_dimensions.group(1, 5, hidden = True)

wb1.save(wp1)
