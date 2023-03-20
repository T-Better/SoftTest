import openpyxl as opx

p = r'D:\Git_Reps\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\anki_1678953594.xlsx'
f2 = r'\anki_20230320.xlsx'

wb1 = opx.load_workbook(p + f2)
ws2 = wb1['2号']

# note = opx.comments.Comment('已完成','chase')
# ws2['A3'].comment = note

# 冻结test.xlsx的Sheet1的第一行
# ws2.freeze_panes = ws2['B1']

# 获取第2列1、3、5、7行的数据
# for i in range(1,8,2):
#     data = ws2.cell(row=i,column=2)
#     print(data.value)

# 复制指定工作表并重新命名
# wst = wb1.copy_worksheet(wb1['3号'])
# wst.title ='3号备份'

# 标题加粗 22号 微软雅黑；正文：宋体 11号；重点：红色加粗倾斜单下划线11号字体
# fh = opx.styles.Font(bold=True, name='微软雅黑')

# fc = opx.styles.Font(name='宋体', size=11)

# fs = opx.styles.Font(bold=True,color='FF0000', italic=True, under_line=True,size=11)

# 求第三行所有数字之和并将结果写入第三行最后一列
# ws2['H3'] = '=sum(A3:H3)'

# 第一行均为双实线对象，第二行及一下所有内部边框均为单实线黑色
# lh = opx.styles.Side(style='double')
# lc = opx.styles.Side(style='thin',color='000000')

# bh = opx.styles.Border(left=lh,right=lh,top=lh,bottom=lh)
# bc = opx.styles.Border(left=lc,right=lc,top=lc,bottom=lc)

# 获取test.xlsx第一个工作表名称并将其重命名为1月
wb1['4号'].title='4号备份'

# wb1.close()
wb1.save(p + f2)
















