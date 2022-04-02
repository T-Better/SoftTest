import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test202111221324.xlsx'

wb1 = opx.Workbook(wp1)  # 创建工作簿

for i in range(1,101):
    wb1.create_sheet(str(i)+'号')  # 创建100张工作表，名为1号、2号等

wb1.save(wp1)
