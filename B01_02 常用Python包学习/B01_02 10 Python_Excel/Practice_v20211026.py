# Practice_v20211026.py
import os
import time
import datetime as dt
# print("-"*10)
# print(os.stat(r'D:\学习\孙兴华《中文讲Python从入门到办公自动化》excel、word、ppt、PDF等 Python自动化 Python办公自动化 Python自动化办公\文档\python零基础入门课件\Python零基础教程\《跟着孙兴华学习Python基础》 - 副本.pptx'))

# print(time.ctime(1635055613))

date1 = dt.datetime.fromtimestamp(1635055613)
print(date1)
print(date1.year,date1.month,date1.day)
print(date1.hour,date1.minute,date1.second)
