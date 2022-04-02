import openpyxl as opx

wpf = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\刘子君 成方金信工作量表.xlsx'
wb1 = opx.load_workbook(wpf)  # 加载该文件
ws1 = wb1['5月']  # 选中5月sheet页
for i in range(1,8,2):
    print(i,ws1.cell(row=i, column = 2).value)
