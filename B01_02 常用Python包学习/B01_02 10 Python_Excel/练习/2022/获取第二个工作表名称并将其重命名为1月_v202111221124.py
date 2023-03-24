import openpyxl as opx

wp2 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\新建100张工作表 1-100号1118.xlsx'
wb2 = opx.load_workbook(wp2)
wss2 = wb2.worksheets
wss2[1].title = '2月'
wb2.save(wp2)
