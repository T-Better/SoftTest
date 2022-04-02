import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test202111231100.xlsx'
wb1 = opx.load_workbook(wp1)
ws2 = wb1['2月']

# 第一步：先创建要用的线
side1 = opx.styles.Side(style='double',color='000000')  # 双实线黑色边框
side2 = opx.styles.Side(style='thin',color='000000')  # 单实线黑色

# 第二步：再由线组成边框
# 四面均为双实线对象
border1 = opx.styles.Border(left=side1,right=side1,top=side1,bottom=side1)
# 四面均为单实线对象
border2 = opx.styles.Border(left=side2,right=side2,top=side2,bottom=side2)

# 第三步：做好的边框应用在指定单元格对象上
# 第二行及一下所有内部边框均为单实线黑色
for i in ws2['A2:Z51']:
    for c in i:
        c.border = border2
# 第一行单元格双实线黑色边框
for j in ws2['A1:Z1']:
    for c in j:
        c.border = border1
# 整体外边框为双实线黑色
for k in ws2['A1:Z51']:
    for c in k:
        c.border = border1

wb1.save(wp1)