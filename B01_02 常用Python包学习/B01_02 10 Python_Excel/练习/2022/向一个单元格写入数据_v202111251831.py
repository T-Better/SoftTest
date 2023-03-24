import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1637828640.xlsx'

wb1 = opx.load_workbook(wp1)
ws1 = wb1['1号']

# 方法一
cell1 = ws1['A12']
cell1.value = '向一个单元格写入数据'
ws1.cell(11,1,value="向一个单元格写入数据方法二")

wb1.save(wp1)