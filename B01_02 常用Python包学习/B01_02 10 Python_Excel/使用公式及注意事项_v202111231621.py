import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test202111231100.xlsx'
# wb1 = opx.load_workbook(wp1)
wb1 = opx.load_workbook(wp1,data_only=True)

ws1 = wb1['1月']
ws1['B6'] = '=sum(C5:O5)'

wb1.save(wp1)