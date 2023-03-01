import time


# 如何用最简单方式输出诸如2023-02-28 12:00:00格式的时间
print(time.strftime('%Y-%m-%d %H:%M:%S'))

# 如何用最简单方式输出如20230228格式的时间
print(time.strftime('%Y%m%d'))

# 将当前的时间戳转成带格式的时间 格式要求如：2021年12月14日 10H:19M:18S
print('{}'.format(time.strftime('%Y年%m月%d日 %HH:%MM:%SS'),time.localtime()))
