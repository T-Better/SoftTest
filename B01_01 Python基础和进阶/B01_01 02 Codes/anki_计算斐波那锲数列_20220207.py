# anki_计算斐波那锲数列_20220207.py
def feb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return feb(n-1) + feb(n-2)

print(feb(6))
