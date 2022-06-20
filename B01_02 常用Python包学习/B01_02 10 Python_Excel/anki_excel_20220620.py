import openpyxl as opx

# 在某个excel的第一个sheet页的第五行前面插入两行
ws1.insert_rows(5,2)

# 移动1-3列1-3行向下移动两行，向右移动一列
ws1.move_ranges('A1:C3',rows=2,cols=1)

