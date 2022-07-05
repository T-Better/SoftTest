import openpyxl as opx

p1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs\{}'.format('test1654591815.xlsx')

wb1 = opx.load_workbook(p1)
ws1 = wb1['1号']
"""
ws1.row_dimensions[1].height = 40
ws1.column_dimension['A'].width = 15
"""

# 第一步：创建要用的线
side1 = opx.styles.Side(style='double',color = '000000')  # 双实线 黑色
side2 = opx.styles.Side(style='thin',color = '000000')  # 单实线 黑色

# 第二步：再由线组成边框
  # 四面均双实线
border1 = opx.styles.Border(left=side1,right=side1,top=side1,bottom=side1)
border2 = opx.styles.Border(left=side2,right=side2,top=side2,bottom=side2)

# 第三步：设置表格边框
for i in ws1['A1:J51']:
    for c in i:
        c.border = border1

for j in ws1['A1:J1']:
    for c in j:
        c.border = border2
wb1.save(p1)

