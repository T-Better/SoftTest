import openpyxl as opx

path1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel'

wb1 = opx.load_workbook(path1)
ws1 = wb1['1月']
ws1.move_range('A1:C3',rows = 2,clos = 1)

# 


wb1.save(path1)
