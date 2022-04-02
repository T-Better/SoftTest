# anki_自动化办公_20220217.py
import openpyxl as opx
import time


wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test202111231100.xlsx'
wb1 = opx.load_workbook(wp1)
ws3 = wb1['3号']

# 1.让标题水平垂直居中且自动换行
ali1 = opx.styles.Alignment(horizontal='center',vertical='center',wrap_text=True)
for i in ws3['A1:J1']:
    for c in i:
        c.alignment = ali1

# 2.让正文自动换行
ali2 = opx.styles.Alignment(wrap_text = True)
for j in ws3['A2:J12']:
    for c in j:
        c.alignment = ali2
wb1.save(wp1)
