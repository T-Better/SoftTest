import openpyxl as opx

path1 = r''
wb1 = opx.load_workbook(path1)
ws1 = wb1['1号']

ws1.row_dimensions[1].height = 40
ws1.col_dimensions['A'].width = 20
wb1.save(wb1)


