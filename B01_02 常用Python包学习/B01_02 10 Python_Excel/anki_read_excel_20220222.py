import openpyxl as opx

path1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\002 Docs\fruit_price_3.xlsx'
wb1 = opx.load_workbook(path1)
ws1 = wb1['Sheet1']

res = []
for col in ws1.iter_cols(min_row=2):
    tmp = []  # 放这：可以每操作完一列就清空列表，继续下一列，从而不会越来越长
    for c in col:
       tmp.append(c.value)
    res.append(tmp)
print(res)
wb1.save(path1)
