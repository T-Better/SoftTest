import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\新建100张工作表03.xlsx'
wb1 = opx.load_workbook(wp1)
# ws1 = wb1['Sheet']
for i in range(1,32):
    ws1 = wb1.copy_worksheet(wb1['9号'])
    ws1.title = str(i)+'月'
wb1.save(wp1)