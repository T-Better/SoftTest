# Practice2_v20211028.py

"""
需求：path = 'D:\学习\孙兴华《中文讲Python从入门到办公自动化》excel、word、ppt、PDF等 Python自动化 Python办公自动化 Python自动化办公'
（1）搜索整个文件夹，包括文件夹中所有的文件夹  # os.listdir()
（2）筛选体积大于2MB的压缩包.zip文件
（3）筛选这些文件中日期早于17日之前的文件
（4）输出这些文件的路径  # glob.glob(path)返回的root
"""
import os
import glob
# import datetime as dt
import time

# # 1.文件大于2M，时间是2022年以前的
# os.chdir('D:\学习\孙兴华《中文讲Python从入门到办公自动化》excel、word、ppt、PDF等 Python自动化 Python办公自动化 Python自动化办公')
# # flist_mp4：所有mp4文件的列表
# flist_mp4 = glob.glob('**/*.mp4',recursive=True)  # **如何就是任意层文件或文件夹呢？**/*又是啥？
# # *代表0或多个字符；**表示任意层文件或文件夹；recursive=true表示查找所有此目录下的文件夹和子文件夹中的文件
# for f in flist_mp4:
#     f_size = os.stat(f).st_size/1024/1024  # os.stat(f)后会返回st_size等，这里再拿取其size换算成m
#     f_year = dt.datetime.fromtimestamp(os.stat(f).st_ctime).year  # 转换格式获取年份
#     if (f_size > 2) and (f_year < 2022):
#         print(f'路径：{f},大小{f_size}.mb，于{f_year}年创建')
#         print("-" * 10)

# 2.文件大于2M，时间是2022年1月之前的
os.chdir('D:\学习\孙兴华《中文讲Python从入门到办公自动化》excel、word、ppt、PDF等 Python自动化 Python办公自动化 Python自动化办公')
flist2_mp4 = glob.glob('**/*.mp4',recursive=True)
for f2 in flist2_mp4:
    f2_size = os.stat(f2).st_size/1024/1024
    f2_time = time.localtime(os.stat(f2).st_ctime)  # time.localtime()可以将时间戳格式化？
    f2_date = time.strftime('%Y-%m-%d',f2_time)
    if (f2_size > 2) and (f2_date < '2022-01-01'):
        print(f'路径:{f2},大小{int(f2_size)}mb,于{f2_date}日创建')
        print("=" * 10)