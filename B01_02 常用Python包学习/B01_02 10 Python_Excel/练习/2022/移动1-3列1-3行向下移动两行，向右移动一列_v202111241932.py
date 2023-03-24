import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1637753231.xlsx'

wb1 = opx.load_workbook(wp1)
ws1 = wb1['2号']

ws1.move_range('A1:C3',rows = 2,cols = 1)

wb1.save(wp1)


