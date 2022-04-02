import openpyxl as opx

f1 = r''
wb1 = opx.load_workbook(f1)
ws1 = wb1['1号']

# 在某个excel的第一个sheet页第五列后面删除1列
ws1.delete_cols(5,1)






