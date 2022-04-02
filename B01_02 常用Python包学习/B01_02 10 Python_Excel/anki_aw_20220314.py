import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test202111231100.xlsx'
wb1 = opx.load_workbook(wp1)
ws3 = wb1['3号']

ali_h = opx.styles.Alignment(horizontal='center', vertical='center',wrap_text=True)
ali_c = opx.styles.Alignment(wrap_text = True)

for r in ws3['A1:J1']:
    for c in r:
        c.alignment = ali_h

for j in ws3['A2:J10']:
    for c in j:
        c.alignment = ali_c

# 在某个excel的第一个sheet页的第五列前面插入两列
ws3.inert_cols(5, 2)

# 设置第一行高30，第一列宽15
ws3.row_dimensions[1].height = 30
ws3.column_dimensions['A'].width = 15

# 在最后一行写入数据
ws3.append(['1','2','3'])

wb1.save(wp1)

