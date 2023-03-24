import openpyxl as opx

p1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
e1 = r'\test1665234028.xlsx'
ep1 = p1+e1
wb1 = opx.load_workbook(ep1)
"""
# 给单元格A1做“已完成”批注
# wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test202111231100.xlsx'

ws1 = wb1['第1号']
note1 = opx.comments.Comment('已完成20221008','claren')
ws1['B2'].comment = note1
wb1.save('wp1')
"""
"""
# 向一个区域内写入数据
ws2 = wb1['第2号']
ws2['A12'].value = '666'
wb1.save(ep1)
"""
"""
# 在最后一行写入数据
ws3 = wb1['第3号']
ws3.append(['20221005','20221006','20021007',20021008,20021009])
wb1.save(ep1)
"""
"""
# 设置第一行高30，第一列宽15
ws4 = wb1['5号']
ws4.row_dimensions[1].height = 30
ws4.column_dimensions['A'].width = 15
wb1.save(ep1)
"""





