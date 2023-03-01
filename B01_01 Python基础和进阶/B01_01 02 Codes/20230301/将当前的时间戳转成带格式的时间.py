"""
time：将当前的时间戳转成带格式的时间 格式要求如：2021年12月14日 10H:19M:18S
"""
import time

nt = time.strftime("%Y年%m月%d日 %HH:%MM:%SS", time.localtime())
print(nt)




