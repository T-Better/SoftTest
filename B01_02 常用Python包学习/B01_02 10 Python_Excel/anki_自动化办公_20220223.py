# 从fruit_price.xlsx中读取数据结
import openpyxl as opx

path1 = r'D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_03 自动化办公\C06_03 02 Excel_Python\002 Docs\fruit_price.xlsx'
wb1 = opx.load_workbook(path1)
ws1 = wb1['Sheet1']
res_list = []

for row in ws1.iter_rows(min_row=2):
    tmp = []
    for c in row:
        tmp.append(c.value)
    res_list.append(tmp)

print(res_list)
