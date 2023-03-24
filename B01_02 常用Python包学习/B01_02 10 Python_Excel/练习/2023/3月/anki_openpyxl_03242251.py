import openpyxl as opx

p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\anki_1678953594.xlsx'
f2 = r'\anki_设置行高列高_20230316.xlsx'

wb1 = opx.load_workbook(p + f1)
ws2 = wb1['2号']
# 标题加粗 22号 微软雅黑；正文：宋体 11号；重点：红色加粗倾斜单下划线11号字体
"""
f1 = opx.styles.Font(name='微软雅黑',size=22,bold=True)
fc = opx.styles.Font(name='宋体',size=11)
fs = opx.styles.Font(italic=True,color='FF0000',under_line='single')
"""

# 求第三行所有数字之和并将结果写入第三行最后一列
ws2['K3'] = '=sum(A3:F3)'

wb1.save(p + f1)



















