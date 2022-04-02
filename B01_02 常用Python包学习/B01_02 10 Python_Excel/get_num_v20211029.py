import re

target = input()  # 想要找的内容

f = open("session.txt","r")
line = f.readline()
line = line[:-1]
while line:  # 直到读完文件
    line = f.readline()  # 读取一行文件，包括换行符
    line = line[:-1]  # 去除换行符
    r = re.match("",line)


f.close()  # 将文件关闭