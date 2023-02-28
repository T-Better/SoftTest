import time

print('{}'.format(time.strftime('%Y%m%d')))  # 20230228
print('{}'.format(time.strftime('%Y-%m-%d %H:%M:%S')))  # 2023-02-28 12:00:00

print('{:30s}{}'.format('time.time()',time.time()))#time.time()返回的是秒数
print('{:30s}{}'.format('time.localtime()',time.localtime()))#localtime 返回的是元组值
print('{:30s}{}'.format('format time.localtime',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))
print('{:30s}{}'.format('time.strftime',time.strftime('%Y-%m-%d %H:%M:%S')))#最简便的输出方法







