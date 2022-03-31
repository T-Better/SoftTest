import pytest
from collections import namedtuple
User = namedtuple('User','name,age,id')
User.__new__.__defaults__ = (None,None,False)

user = User('lisi','18','22')

@pytest.mark.parametrize('name',['xiaoming','xiaohong'])
def test_step1():
    print("1")
    assert 1 == 1

@pytest.mark.parametrize(("user","password"),[("zhangsan","zhangsan123"),("xiaoming","xiaoming123")])
def test_step2():
    print("2")
    assert 2 == 1
