import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1637753231.xlsx'

wb1 = opx.load_workbook(wp1,data_only=True)
ws4 = wb1['4号']

ws4['K2'] = '= sum(A2:J2)'

wb1.save(wp1)

