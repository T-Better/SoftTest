import openpyxl as opx
import re

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1637828640.xlsx'

wb1 = opx.load_workbook(wp1)
ws5 = wb1['5号']

ws5.insert_cols('E1',2)

# 复制指定工作表9月
ws1 = wb1.copy_worksheet('9月')
ws1.title=""

# 获取test.xlsx第一个工作表名称并将其重命名为1月
wss1 = wb1.worksheets
wss1[0].title='1月'

# 使用默认方式激活第一个工作表
wb1.active

# 在某个excel的第一个sheet页的第五列前面插入两列
ws5.insert_cols('E1',2)

# 查询第二行第四列的位置结果，行返回2，列返回D
ncw = opx.utils.get_column_letter(2)
wcn = opx.utils.column_index_from_string('D')
print(ncw,wcn)

# 冻结excel的第一行
ws5.freeze_panes("A2")

ws5.freeze_panes("B1")
wb1.save(wp1)