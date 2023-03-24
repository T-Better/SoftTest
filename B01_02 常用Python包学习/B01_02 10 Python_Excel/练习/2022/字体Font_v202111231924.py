import openpyxl as opx

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test202111231100.xlsx'

wb1 = opx.load_workbook(wp1)
ws2 = wb1['2月']
font_header = opx.styles.Font(name=u'微软雅黑', bold=True, size=22)  # 标题:
for i in  ws2['A1:Z1']:
    for c in i:
        c.font = font_header  # 标题加粗 22号 微软雅黑

font_content = opx.styles.Font(name=u'宋体', size=11)  # 正文
for j in ws2['A2:Z50']:  # 因为只能做用于一个单元格对象
    for c in j:  # 而j是一(元)组单元格，一个对象
        c.font = font_content  # 正文：宋体 11号

# 重点：红色加粗倾斜单下划线11号字体
font_mark = opx.styles.Font(name=u'宋体',bold=True,size=11, italic=True,
                            underline='single', color='FF0000') 
for k in ws2['A5:Z5']:
    for c in k:
        c.font = font_mark  # 第五行：红色加粗倾斜单下划线11号字体

wb1.save(wp1)
