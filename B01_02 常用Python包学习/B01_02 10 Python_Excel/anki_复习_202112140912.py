import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1637828640.xlsx'
wb1 = opx.load_workbook(wp1)
ws6 = wb1['6号']

# 删除除9号外的工作表
wss5 = wb1.worksheets
for i in wss5:
    if i.title != "9号":
        wb1.remove(i)
    else:
        continue

# 新建指定工作表4月
wb1.create_sheet("4月")


wb1.save(wp1)