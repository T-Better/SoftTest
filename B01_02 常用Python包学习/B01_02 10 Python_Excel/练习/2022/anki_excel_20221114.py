import openpyxl as opx

p1 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs'
e1 = r'anki_1665474080.xlsx'
ep1 = p1+e1

wb1 = opx.load_workbook(ep1)
ws1s = wb1.worksheets
for i in ws1s:
    if i.title !='9号':
        wb1.remove(wb1[i.value])
    else:
        continue
wb1.save(wb1)











