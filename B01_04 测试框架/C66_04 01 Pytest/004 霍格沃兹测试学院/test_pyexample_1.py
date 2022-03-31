def add(x,y):
    return x+y

def test_add():
    assert add(1,2) == 3

def test_add2():
    print("i am 2")
    assert add(1.2,3.1) == 4.3