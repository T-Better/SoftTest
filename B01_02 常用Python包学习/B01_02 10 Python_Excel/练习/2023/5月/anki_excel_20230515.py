import openpyxl as opx


# 两个方法向指定一个单元格写入数据
# ws1['A1'] = 'B1'
# ws1.cell(1,3,value='B1')

p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\anki_1678953594.xlsx'
f2 = r'\anki_设置行高列高_20230316.xlsx'

wb1 = opx.load_workbook(p+f1)
ws1 = wb1['1号']
# 第一行 双实线 黑色
s1 = opx.styles.Side(style='double',color = '000000')
b1 = opx.styles.Border(top=s1,bottom=s1, left=s1,right=s1)
for h in ws1['A1':'J1']:
    for c in h:
        c.border = b1

# 后面几行
# TODO
# TODO
for t in ws1['A2':'J10']:
    for c in t:
        pass # TODO

wb1.save(p+f1)






