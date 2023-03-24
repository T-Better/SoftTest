import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test.xlsx'

wb1 = opx.load_workbook(wp1)
ws1 = wb1['Sheet']

ncw = opx.utils.get_column_letter(2)
print(ncw)

wcn = opx.utils.column_index_from_string('D')
print(wcn)
