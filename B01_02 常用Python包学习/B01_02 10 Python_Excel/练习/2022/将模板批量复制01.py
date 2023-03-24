import openpyxl as opx

cwp = 'D:\\BaiduNetdiskWorkspace\\Super_coder\\O03_Office_Auto_My_code\\Excel_001_读写excel\\a\\批量修改工作表的名称.xlsx'

wb1 = opx.load_workbook(cwp)

for i in range(1,32):
    cl1 = wb1.copy_worksheet(wb1['Sheet1'])  # 先将Sheet1复制内容命名为cl1
    cl1.title = '7月'+str(i) + '日'  # 然后将cl1的名称改名为7月i[1-31]日
wb1.remove(wb1['Sheet1'])  # 删除原模板
wb1.save('将模板批量复制01.xlsx')  # 保存