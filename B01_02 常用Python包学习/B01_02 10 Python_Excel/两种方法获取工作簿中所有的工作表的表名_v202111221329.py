import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test202111221324.xlsx'
wb1 = opx.load_workbook(wp1)

# 方法一
# wss1 = wb1.worksheets
# for i in wss1:
#     print(i.title, end="|")

wss2 = wb1.sheetnames
for i in wss2:
    print(i, end = "||")
wb1.close