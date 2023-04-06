import openpyxl as opx

p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\anki_1678953594.xlsx'

wb1 = opx.load_workbook(p+f1)
ws3 = wb1['3号']

# 求第三行所有数字之和并将结果写入第三行最后一列
ws3['G3'] = '=sum(A3,F3)'

# 给一下目录中的某个excel单元格A1做“已完成”批注
n1 = opx.comments.Comment('已完成','lzj')
ws3['A1'].comment = n1

# 在最后一行写入数据
ws3.append(['a','b'])

# 从第2行开始按行读取数据，有几行读取几行
r = []
for r in ws3.iter_row(min_row=2):
    l = []
    for c in r:
        l.append(c.value)
print(r)

wb1.save(p+f1)

















