import openpyxl as opx

wpf = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\刘子君 成方金信工作量表.xlsx'

# 根据列的数字返回字母
ncw = opx.utils.get_column_letter(2)
print(ncw)
# 根据字母返回列的数字
wcn = opx.utils.column_index_from_string('D')
print(wcn)