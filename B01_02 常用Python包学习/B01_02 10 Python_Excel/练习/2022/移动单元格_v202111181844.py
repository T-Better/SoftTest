import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test.xlsx'

wb1 = opx.load_workbook(wp1)
ws1 = wb1['Sheet']
ws1.move_range("B2:Z2",rows=-1,cols=-1)  # 将第二行数据向左上移动一行一列
wb1.save(wp1)