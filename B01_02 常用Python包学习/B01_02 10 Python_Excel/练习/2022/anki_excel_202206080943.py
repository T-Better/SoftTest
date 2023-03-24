import openpyxl as opx

p1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs\{}'.format('test1654591815.xlsx')
"""
1.让标题水平垂直居中且自动换行
2.让正文自动换行
"""
wb1 = opx.load_workbook(p1)
ws2 = wb1['第2号']
ali1 = opx.styles.Alignment(horizontal='center',vertical='center',wrap_text=True)
ali2 = opx.styles.Alignment(wrap_text = True)

for i in ws2['A1':'J1']:
    for c in i:
        c.alignment = ali1

for j in ws2['A2':'J12']:
    for c in j:
        c.alignment = ali2

# 给单元格A1做“已完成”批注
note1 = opx.comments.Comment('已完成','lzj')
ws2['C1'].comment = note1

# 冻结test.xlsx的Sheet1的第一行
ws2.freeze_panes = 'A2'

# 求第三行所有数字之和并将结果写入第三行最后一列
ws2['K3'] = '=sum(A3,J3)'

# 两个方法向指定一个单元格写入数据
ws2['K4'].value = "K4"
ws2.cell('K',5,value='写入数据1')

wb1.save(p1)



