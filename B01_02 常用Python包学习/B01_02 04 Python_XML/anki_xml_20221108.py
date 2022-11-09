
"""
import os

for i in os.scandir('path'):
    if i.name.endswith('.xls'):
        print(i.name,i.path,i.is_dir())
"""

# 两个方法向指定一个单元格写入数据
import openpyxl as opx

e1 = ''
p1 = ''
ep1 = p1+e1
wb1 = opx.load_workbook(ep1)
ws1 = wb1['1号']
# 法1
ws1['A1'] = '1'
ws1.cell(1,5,value='note')

# 将模板批量复制 将Sheet1复制31份，然后删除Sheet1模板
for i in range(1,32):
    ce = wb1.copy_worksheet(wb1['1号'])
    ce.title = '7月'+str(i)+'日'
wb1.remove(wb1['1号'])
wb1.save(p1)



