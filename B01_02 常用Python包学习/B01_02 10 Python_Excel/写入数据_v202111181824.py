import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test.xlsx'
wb1 = opx.load_workbook(wp1)
ws1 = wb1['Sheet']
i = 1
for r in ws1['A1:Z20']:  # 遍历该区域内的每一行
    for ce in r:  # 遍历每行中的每个单元格
        ce.value = i
        i += 1

wb1.save(wp1)