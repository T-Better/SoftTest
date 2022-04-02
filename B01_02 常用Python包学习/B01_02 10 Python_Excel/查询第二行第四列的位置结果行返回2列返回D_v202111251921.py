import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1637753231.xlsx'

wb1 = opx.load_workbook(wp1)
ws5 = wb1['5号']

# 根据猎的数字返回字母
ncw = opx.utils.get_column_letter(2)
print(ncw)

wcn = opx.utils.column_index_from_string('D')
print(wcn)

wb1.close()