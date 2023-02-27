# 10！=10*9*8...=3628800


def fact(n, res):
    while n > 0:
        res = res * n
        n = n - 1
    return res


if __name__ == "__main__":
    print(fact(10, 1))
