i = 1

while i <= 10:
    res = 'set name{} zhangsan{}'.format(i,i)
    print(res)
    with open('./datas_02.txt', 'a') as f:
        f.write(res)
        f.write('\n')
    i = i + 1
