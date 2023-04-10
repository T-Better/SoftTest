import openpyxl as opx

p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\anki_1678953594.xlsx'
f2 = r'\anki_设置行高列高_20230316.xlsx'

wb1 = opx.load_workbook(p + f1)
ws2 = wb1['2号']
# 获取test.xlsx第一个工作表名称并将其重命名为1月
ws2.title='2月'

# 获取第2列1、3、5、7行的数据
for i in range(1,8,2):
    print(ws2.cell(row=i, column=2).value)

# 微软雅黑 11号 红色 加粗 倾斜 单下划线
ali1 = opx.styles.Alignment(name=u'微软雅黑', size=11, color='FF0000',bold=True,italic=True, underline='single')

# 在最后一行写入数据
ws2.append(['a','b'])








wb1.save(p+f1)
# wb1.close()
