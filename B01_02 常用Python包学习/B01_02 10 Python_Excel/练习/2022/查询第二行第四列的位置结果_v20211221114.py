import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test.xlsx'

wb1 = opx.load_workbook(wp1)
ws1 = wb1['Sheet']

gcw = opx.utils.get_column_letter(4)  # 获取列的位置，返回为字母

grp = opx.utils.column_index_from_string('B')  # 获取行数，返回为数字
print(gcw,grp)
wb1.close()