# openpyxl练习
import openpyxl as opx

p = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
f1 = r'\anki_1678953594.xlsx'
f2 = r'\anki_设置行高列高_20230316.xlsx'

wb1 = opx.load_workbook(p + f1)
ws2 = wb1['2号']

# 获取第2列1、3、5、7行的数据
# TODO

# 给一下目录中的某个excel单元格A1做“已完成”批注
# TODO

# 复制指定工作表并重新命名
# ws4 = wb1.copy_worksheet(wb1['5号'])
# ws4.title = '5号备份'

# 移动1-3列1-3行向下移动两行，向右移动一列
# TODO

# 冻结test.xlsx的Sheet1的第一行
# ws2.freeze_panes = 'A2'

# 在某个excel的第二个sheet页第五列后面删除1列
# ws2.delete_cols(5,1)

# 标题加粗 22号 微软雅黑；正文：宋体 11号；重点：红色加粗倾斜单下划线11号字体
# TODO

# 求第三行所有数字之和并将结果写入第三行最后一列
# ws2['K4'] = '=sum(A4:J4)'

# 除了9月份的工作表以外都删除
# wb1.remove(wb1['1号'])

# 获取test.xlsx第一个工作表名称并将其重命名为1月
# wb1['3号'].title='3月'

# 设置第一行高30，第一列宽15
# TODO

# 按行 按列取数据
# TODO

wb1.save(p+f1)


