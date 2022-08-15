import openpyxl as opx

wb1 = opx.load_workbook('./DOCS/test.xlsx')
# wss = wb1.worksheets
# for w in wss:
#     print(w.title)
ws1 = wb1['Sheet2']
for c in range(1,8,2):
    print(c,ws1.cell(row=i,column=2).value)





