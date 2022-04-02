import openpyxl as opx
import os

# cwp：当前工作路径
cwp = 'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a'
os.chdir(r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a')

wb1 = opx.load_workbook(r"新建100张工作表01.xlsx")  # 加载指定xlsx
wss = wb1.worksheets# 获取表名
j = 1
for i in wss:
    # ws1 = wb1.worsheet(i)  # 将表名的字符串指向表
    i.title = str(j) + "月" # i:<Worksheet "第1天"> 需要i.title将第1天取出
    j = int(j) + 1
wb1.save('批量修改工作表的名称.xlsx')