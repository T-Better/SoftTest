import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\新建100张工作表02.xlsx'

# 加载工作表
wb2 = opx.load_workbook(wp1)
# 获取所有工作表
wss2 = wb2.sheetnames
print(wss2)  

for i in wss2:
    # 遍历该工作簿中所有的工作表，如果不是9号工作表，将其删除
    if i != "9号":
        ws = wb2[i] # i只是一个字符串，没有指定到sheet，需要先指向sheet，然后去remove
        wb2.remove(ws)
    else:
        continue
wb2.save(r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\新建100张工作表03.xlsx')
