import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test202111231100.xlsx'
wb1 = opx.load_workbook(wp1)
ws1 = wb1['1号']
not1 = opx.comments.Comment('已完成','lzj')
ws1['A1'].comment = not1
wb1.save(wp1)
