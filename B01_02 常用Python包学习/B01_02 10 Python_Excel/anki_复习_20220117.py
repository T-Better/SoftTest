import openpyxl as opx

path1 = ''
wb1 = opx.load_workbook(path1)
ws1 = wb1('1月')

# 1.获取1-3列，1-5行数据，分别使用按行、按列、区域3种方法法
# 一
for i in ws1['A1:C5']:
    for c in i:
        print(c.value)

# 二
for j in ws1.iter_rows(min_row=1,max_row=5,min_col=1,max_col=3):
    for c in j:
        print(c.value)
# 三
for k in ws1.iter_cloumns(min_row=1,max_row=5,min_col=1,max_col=3):
    for c in k:
        print(c.value)

# 删除除9号外的工作表
wss = wb1.worksheets
for i in wss:
    if i.title != '9号':
        wb1.remove(i)

wb1.save(path1)
