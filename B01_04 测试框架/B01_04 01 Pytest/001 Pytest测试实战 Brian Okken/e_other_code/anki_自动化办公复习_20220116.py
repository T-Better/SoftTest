import openpyxl as opx

path1 = ''
wb1 = opx.load_workbook(path1)
wb1.create_sheet('4月')
ws1 = wb1['4月']
note1 = opx.comments.Comment('已完成','lzj')
ws1['A1'].comment = note1

# 设置第一行高30，第一列宽15
ws1.rows_dimensions[1].height = 30
ws1.columns_dimensions['A'].width = 15

wb1.save('path1')

