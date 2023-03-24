import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1640048977.xlsx'
wb1 = opx.load_workbook(wp1)
ws2 = wb1['2号']

ws2.move_range()
