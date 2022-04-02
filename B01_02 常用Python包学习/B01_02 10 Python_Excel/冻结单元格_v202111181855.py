import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test.xlsx'

wb1 = opx.load_workbook(wp1)
ws1 = wb1['Sheet']
ws1.freeze_panes="A2"  # 冻结第一行
ws1.freeze_panes='B1'  # 冻结第一列
wb1.save(wp1)
