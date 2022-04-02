# 新建指定工作表4月
import openpyxl as opx

wb1 = opx.load_workbook('')
wb1.create_sheet('3月')
wb1.save()