import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\新建100张工作表02.xlsx'
wb1 = opx.Workbook(wp1)  # 打开工作簿
for i in range(1,101):  # 创建100张工作表
    wb1.create_sheet(str(i)+"号")
wb1.save(wp1)
