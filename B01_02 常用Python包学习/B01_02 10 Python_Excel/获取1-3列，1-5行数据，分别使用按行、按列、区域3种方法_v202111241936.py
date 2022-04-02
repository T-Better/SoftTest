import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1637753231.xlsx'

wb1 = opx.load_workbook(wp1)
ws3 = wb1['3号']

# 方法一：
for i in ws3['A1':'E3']:
    for c in i:
        print(c.value, end=" ")
print("/n")

# 方法二：
for j in ws3.rows:
    for c in j:
        print(c.value, end="|")
print("/n")

for k in ws3.columns:
    for c in k:
        print(c.value, end="||")

wb1.close()