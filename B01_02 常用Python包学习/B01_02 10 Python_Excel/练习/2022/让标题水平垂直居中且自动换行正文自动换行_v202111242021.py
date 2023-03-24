import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1637753231.xlsx'

wb1 = opx.load_workbook(wp1)
ws6 = wb1['6号']

# 让标题水平垂直居中且自动换行
ali1 = opx.styles.Alignment(horizontal='center',vertical='center',wrap_text=True)
for i in ws6['A1:Z1']:
    for c in i:
        c.alignment = ali1

# 让正文自动换行
ali2 =opx.styles.Alignment(horizontal='general',wrap_text=True)
for j in ws6['A2:Z49']:
    for c in j:
        c.alignment = ali2

