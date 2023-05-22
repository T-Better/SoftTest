def seq(nu):
    for i in range(nu):
        i = i * 3
        yield i

g = seq(3)
next(g)


