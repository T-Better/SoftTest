import openpyxl as opx

p = r'$git_reps\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\fruit_price.xlsx'

wb1 = opx.load_workbook(p + f1)
ws1 = wb1['Sheet1']

r = []  # 把所有列表放进来
# 从第2行开始按行读取数据，有几行读取几行
for r in ws1.iter_rows(min_row=2):
    # 按行读取，从第二行开始
    tmp = []  # 用于按行存取
    for c in r:  # 按行读取后再单个拿出来放到列表中
        tmp.append(c.value)
    r.append(tmp)

wb1.close()











