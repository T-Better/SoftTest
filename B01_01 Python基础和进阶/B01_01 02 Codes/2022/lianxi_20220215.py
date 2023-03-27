# def solution(list_a: list, list_b: list) -> bool:
def solution(list_a, list_b):
    flag = 1
    for i in list_a:
        if i not in list_b:
            flag = 0
        else:
            continue
    return flag


if __name__ == "__main__":
    list_a = [["a", "c"], "b"]
    list_b = [["c", "b"], "b"]
    flag_r = solution(list_a, list_b)
    if flag_r == 0:
        print('false')
    elif flag_r == 1:
        print('true')

# assert solution(["a", "c", "b"], ["c", "b", "a"]) => true
# assert solution(["a", "c", "b"], ["c", "b"]) => false
# assert solution([["a", "c"], "b"], [["c", "b"], "b"]) => false
