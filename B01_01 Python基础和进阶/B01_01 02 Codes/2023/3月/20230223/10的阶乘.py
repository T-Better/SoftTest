# 10!=10*9*8*7*6*5*4*3*2*1

def fact(n,r):
    while n >0:
        r = n * r
        n = n-1
    return r


if __name__ == "__main__":
    print(fact(10,1))


