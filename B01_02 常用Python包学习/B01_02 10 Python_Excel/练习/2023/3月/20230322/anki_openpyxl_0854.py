import openpyxl as opx

p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\fruit_price.xlsx'

wb1 = opx.load_workbook(p + f1)
ws1 = wb1['Sheet1']

# 从第2行开始按行读取数据，有几行读取几行
# r = []  # 用来存类似于[[],[]]
# for r in ws1.iter_rows(min_row=2):  # r:一行多个单元格对象
#     t = []  # 用来装一行的多个内容
#     for c in r: # 读取单个单元格
#         t.append(c.value)
#     r.append(t)

# 冻结test.xlsx的Sheet1的第一行
ws1.freeze_panes = 'A2'

wb1.close()









