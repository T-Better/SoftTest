import openpyxl as opx

p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\anki_1678953594.xlsx'
f2 = r'\anki_设置行高列高_20230316.xlsx'

wb1 = opx.load_workbook(p + f1)
ws2 = wb1['2号']

# 获取第2列1、3、5、7行的数据
l = []
for i in range(1,8,2):
    l.append(ws2.cell(row=i,column=2).value)

# 标题水平垂直居中且自动换行
ali1 = opx.styles.Alienment(vertical='center',horizontal='center',wrap_text = True)
for h in ws2["A1:J1"]:
    for c in h:
        c.alignment = ali1

print(l)
wb1.close()
