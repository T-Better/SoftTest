import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1637753231.xlsx'

wb1 = opx.load_workbook(wp1)
ws5 = wb1['5号']

note1 = opx.comments.Comment('已完成','lzj')
ws5['A1'].comment = note1

wb1.save(wp1)