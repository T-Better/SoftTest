# anki_复习autowork_20220128.py
import openpyxl as opx

path1 = r''
wb1 = opx.load_work(path1)
ws1 = wb1['1号']

ws1.row_dimensions[1].height = 30
ws1.column_dimensions['A'].width = 15

wb1.save('paht1')
