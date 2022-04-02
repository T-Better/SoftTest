# Doc_dir_01_chpath_v20211024.py

import os

cdir = os.scandir(r'D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Python_Auto_Office')
for file in cdir:
    print(file.name,file.stat,end=" | ")
