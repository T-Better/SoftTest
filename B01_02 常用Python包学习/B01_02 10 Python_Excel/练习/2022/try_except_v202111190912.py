try:
    n = int(input())
    if n >= 60:
        print("及格")
    elif n < 60:
        print("不及格")
    elif n > 100:
        print("输入超出了满分")
except(ValueError):
    print("输入错误") 

