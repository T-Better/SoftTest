import openpyxl as opx
import os
# wp:工作路径
wp = 'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\\a'
# 修改当前工作路径，用来保存文件
os.chdir(r'D:\\BaiduNetdiskWorkspace\\Super_coder\\O03_Office_Auto_My_code\\Excel_001_读写excel\\a')
print(os.getcwd())  # 获取修改后的工作路径

# 创建工作簿：实例化openpyxl
wb1 = opx.Workbook()

# 创建工作工作表
i = 1
while i<100:
    wb1.create_sheet("第"+str(i)+"天")  # 创建工作表
    i = i+1
wb1.save("新建100张工作表01.xlsx")
