import xlrd

xlsx1 = xlrd.open_workbook("7月下旬入库表.xlsx")

sheet2 = xlsx1.sheet_by_index(1)

res1 = sheet2.cell_value(1, 2)

print(res1)

# print(sheet2.cell_value(1,2))