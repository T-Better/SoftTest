import openpyxl as opx

fn1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\刘子君 成方金信工作量表.xlsx'
wb1 = opx.load_workbook(fn1)  # 加载工作簿
ws1 = wb1['5月']
cell1 = ws1['A1'].value  # 读取A1表格中的数据给cell1
print(cell1)