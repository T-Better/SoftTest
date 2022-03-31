#test_pyexample_rerun.py 
import random

def add(x,y):
    return x+y

def test_add():
    assert add(1,2) == 3

def test_add2():
    random_value = random.randint(2,5)
    print("random_value"+str(random_value))
    assert random_value == 3
