# 除了9月份的工作表以外都删除
import openpyxl as opx


path1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test202111231100.xlsx'
wb1 = opx.load_workbook(path1)
ws1 = wb1['1月份']
wss = wb1.worksheets

for i in wss:
    if i.title != '9月份':
        wb1.remove(i.title)
    else:
        continue
# 复制指定工作表9月
ws9 = wb1.copy_worksheet(wb1['9月'])

"""
1.让标题水平垂直居中且自动换行
2.让正文自动换行
"""
ali1 = opx.styles.Alignment(horizontal='center',vertical='center',warp_text = Ture)
ali2 = opx.styles.Alignment(warp_text = True)

for i in ws1['A1:J1']:
    for c in i:
        c.alignment = ali1
for j in ws1['A2:J10']:
    for c in j:
        c.alignment = ali2

# 新建100张工作表 1-100号
for k in (1,101):
    wb1.create_sheet(str(i) + '号')

# 将模板批量复制 将Sheet1复制31份，然后删除Sheet1模板

for i in range(1,32):
    ws_c = wb1.copy_worksheet(wb1['Sheet1'])
    ws_c.title = '7月' + str(i) + '日'
wb1.remove(wb1['Sheet1'])
wb1.save(path1)

