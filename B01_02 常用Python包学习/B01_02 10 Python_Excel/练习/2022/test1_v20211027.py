# test1_v20211027.py

import os
import glob

os.chdir('D:\BaiduNetdiskWorkspace\Work\C-人行-浪潮\C00-浪潮 人行事务\C03_文档')
print(glob.glob('z*[0-9]a.txt'))  # 匹配zzz20121027a.txt和zzz6a.txt文件
print("+"*5)
reslist = glob.glob('**/*.xlxs')
print(reslist)
print("="*5)
for f in reslist:
    print(f)
    print("-"*5)