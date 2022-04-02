import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test.xlsx'

wb1 = opx.load_workbook(wp1)
ws1 = wb1['Sheet']
ws1.insert_rows(1,1)  # 在第一行之前插入一行
ws1.insert_cols(1,1)  # 在第一列之前插入一列
ws1.delete_rows(3,1)  # 删除第三行
ws1.delete_cols(3,1)  # 删除第三列
wb1.save(wp1)
