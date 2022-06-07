import openpyxl as opx
import datetime as dt
import random
import os

now_time_stamp = str(int(dt.datetime.now().timestamp()))  # 获取当前时间戳小数点前面的内容

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test{}.xlsx'.format(now_time_stamp)
# p2 = r'D:\Git_Reps\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs\test{}.xlsx'.format(now_time_stamp)
p2 = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_02 常用Python包学习\B01_02 10 Python_Excel\002 Docs\test{}.xlsx'.format(now_time_stamp)
print(wp1)

# 创建工作簿
wb1 = opx.Workbook()

# 创建模板工作表1号
ws1 = wb1.create_sheet()
ws1.title = '1号'

# 将工作簿第一行写数据：标题
for i in ws1['A1':'J1']:
    for c in i:
            c.value = '标题'

# 创建2-10行，1-10列，内容为随机数字
for j in ws1['A2':'J10']:
    for c in j:
        c.value = random.randint(1,1000)
# 删除第一个Sheet
ws0 = wb1['Sheet']
wb1.remove(ws0)

# 然后复制“1号”工作表10份
for i in range(1,11):
    ws2 = wb1.copy_worksheet(ws1)
    ws2.title = "{}号".format(i+1)

wb1.save(p2)
