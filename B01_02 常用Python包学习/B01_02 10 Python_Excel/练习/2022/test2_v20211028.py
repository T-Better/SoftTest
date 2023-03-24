# test2_v20211028.py

import os

if not os.path.exists('D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Python_Auto_Office\\test20211028'):
    # 如果路径存在，则返回true，此时就去执行if内的内容，所以这里要not true去跳出if
    os.mkdir('D:\BaiduNetdiskWorkspace\Super_coder\O03_Office_Auto_My_code\Python_Auto_Office\\test20211028')
else:
    print("路径存在")

