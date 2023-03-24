import openpyxl as opx

wpf = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\刘子君 成方金信工作量表.xlsx'
wb1 = opx.load_workbook(wpf)
ws1 = wb1['5月']
ca = ws1['A1:B2']  # ca：((第一行整体对象),(第二行整体对象))
print(ca)
for o in ca:
    print(o)  # o：一行整体 属性对象
    for j in o:  # j：一行中的一个单元格 属性对象
        print(j.value)  # j.value：一个单元格对应的数值

