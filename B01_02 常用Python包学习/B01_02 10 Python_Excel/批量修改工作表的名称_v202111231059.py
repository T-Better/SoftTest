import openpyxl as opx
import random

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test202111231100.xlsx'
wb1 = opx.load_workbook(wp1)
# for i in range(1,101):
#     ws1 = wb1.create_sheet()
#     ws1.title = str(i)+"月"
# ws1 = wb1.active
ws1 = wb1['1月']
# ws1.freeze_panes='A2'
ws1.move_range('A1:C3',2,1)


wb1.save(wp1)

