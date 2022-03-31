# test_pyexample_1.py 
import time

def add(x,y):
    return x+y

def test_add():
    assert add(1,2) == 3

def test_add2():
    print('i am 2')
    time.sleep(3)
    assert add(1.2,3.1) == 5.3
    assert add(1,2) == 3
