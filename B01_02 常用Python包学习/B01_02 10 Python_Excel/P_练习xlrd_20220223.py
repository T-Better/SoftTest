import xlrd

path2 = r'002 Docs\练习_20220223.xls'
# 获取工作簿对象:xlrd.open_workbook()
wb1 = xlrd.open_workbook(path2)  # 打开工作表

# 获取多个工作表（sheet）对象
wss = wb1.sheet_names()  # 获取所有sheet页名字，返回其列表
print(wss)

# 获取指定单个工作表对象
ws1 = wb1.sheet_by_name('1号')  # 根据sheet页名字获取指定表，返回sheet对象
ws2 = wb1.sheet_by_index(1)  # 根据sheet索引获取对应sheet表（索引从0开始的），返回一个sheet对象
print(ws1, ws2)

# 获取sheet名称
ws1_name = ws1.name
print("sheet1名称：{}".format(ws1_name))

# 获取行数和列数
ws1_rows_num = ws1.nrows  # 获取表格总行数
ws1_cols_num = ws1.ncols  # 获取表格总列数
print("行数：{};列数：{}.".format(ws1_rows_num, ws1_cols_num))

# 获取整行或整列的值（数组）：row_values、col_values
row_values = ws1.row_values(0)  # 获取第一行内容，返回一个列表
col_values = ws1.col_values(0)  # 获取第一列内容，返回一个列表
print("第一行内容：{};第一列内容：{}。".format(row_values, col_values))

# 获取指定单元格的值:第二行第一列
c2a = ws1.cell(1, 0).value
ca2 = ws1.row(1)[0].value
print("第二行第一列值为{}or{}".format(c2a, ca2))

# 获取单元格数据类型 ctype
c2at = ws1.cell(1, 0).ctype
print("第二行第一列单元格内容类型为：{}".format(c2at))

