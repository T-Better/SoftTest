import openpyxl as opx

wp2 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\新建100张工作表02.xlsx'
wb2 = opx.load_workbook(wp2)

wss2 = wb2.worksheets
for i in wss2:
    if i.title != '9号':
        wb2.remove(i)
    elif i.title == '3号':
        continue
wb2.save(wp2)