# Practice2_v20211026.py
import os

j = 0
for path,cdirlist,filelist in os.walk(r'D:\\BaiduNetdiskWorkspace\\Work\\C-人行-浪潮\\C00-浪潮 人行事务\\C03_文档'):
    print(path)
    print(cdirlist)
    print(filelist)
    for i in filelist:
        print(path+i)
        j += 1

print(f'共发现{j}个文件')