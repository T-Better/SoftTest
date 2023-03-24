# anki_自动化办公_20220216.py
import openpyxl as opx
import time


wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test202111231100.xlsx'
wb1 = opx.load_workbook(wp1)
ws3 = wb1['3号']
atime='1592442400'
# 批量修改工作表的名称 将新建100张工作表01.xlsx中第1-100天工作表名改为1-100月
wss = wb1.worksheets
for i in wss:
    i.title = ""
