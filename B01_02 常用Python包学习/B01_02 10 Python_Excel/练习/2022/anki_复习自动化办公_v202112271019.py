import openpyxl as opx
import os

wp1 = r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Excel_001_读写excel\a\test1640048977.xlsx'
wb1 = opx.load_workbook(wp1)
ws2 = wb1['2号']

# windows如何检测a路径下的b文件是否存在，存在和不存在分别返回什么？
os.path.exists(r'a/b')

# 如何通过os遍历文件夹（win要求返回该文件的详细参数），主要返回什么？
a = os.walk(wp1)
for i in a:
    print(i)

# win如何一次创建多层路径的目录文件夹:a/b/c/d
os.makedirs(r'a/b/c/d')
