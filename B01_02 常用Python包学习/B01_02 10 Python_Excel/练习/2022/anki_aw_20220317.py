import openpyxl as opx

path1 = ''
wb1 = opx.load_workbook(path1)
ws1 = wb1['1号']

cs1 = wb1.copy_worksheet(wb1['1号'])
cs1.title = 'name1'
wb1.save(path1)

