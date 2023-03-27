# 1.如何捕获所有错误并将其输出？
try:
    pass
except Exception as res:
    print(res)
    pass

# 2.如何捕获一个或两个错误如NameError、ValueError并将其输出？
try:
    pass
except(NameError,ValueError) as r:
    print(r)


