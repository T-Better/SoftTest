def feb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return feb(n-1) + feb(n-2)

print(feb(6))
