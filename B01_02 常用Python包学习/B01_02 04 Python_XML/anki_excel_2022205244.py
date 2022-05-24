import openpyxl as opx

p1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs\test1653298329.xlsx'
wb1 = opx.load_workbook(p1)
ws1 = wb1['9号']

side1 = opx.styles.Side(style='double', color = '000000')
side2 = opx.styles.Side(style='thin', color = '000000')

border1 = opx.styles.Border(left=side1,right=side1,top=side1,bottom=side1)
border2 = opx.styles.Border(left=side2,right=side2,top=side2,bottom=side2)

for i in ws1['A2:Z10']:
    for c in i:
        c.border = border2

for j in ws1['A1:Z1']:
    for c in j:
        c.border = border1

for k in ws1['A1:Z10']:
    for c in k:
        c.border = border1

wb1.save(p1)
