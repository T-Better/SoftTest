# 循环打印"Hello,World!"的每个字符循环5次。


def circulate_print(str, count=0):
    if count == 5:
        return
    for char in str:
        print(char,end=' ')

    circulate_print(str,count=count+1)


if __name__ == '__main__':
    str = "Hello,World!"
    circulate_print(str)