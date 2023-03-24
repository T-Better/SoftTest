# anki_自动化办公_20220214.py
import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test202111231100.xlsx'
wb1 = opx.load_workbook(wp1)
ws3 = wb1['3号']

note1 = opx.comments.Comment('已完成','lzj')
ws3['A1'].comment = note1

wb1.save(wp1)
