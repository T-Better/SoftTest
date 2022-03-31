import openpyxl as opx

path1 = r''
wb1 = opx.load_workbook(path1)
ws1 = wb1['1月']

# 向一个区域内写入数据
for i in ws1['A1:C3']:
    for c in i:
        c.value = '张三'
        
wb1.close(path1)
