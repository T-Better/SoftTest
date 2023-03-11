def feb(n):
    if n ==1:
        return 1
    if n == 2:
        return 2
    return feb(n-1) + feb(n-2)

print(feb(5))