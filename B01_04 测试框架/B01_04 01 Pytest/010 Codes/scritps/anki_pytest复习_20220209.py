# anki_pytest复习_20220209.py
import pytest

@pytest.mark.run(order=1)
def test_step1():
    print("1")
    assert 1 == 1

@pytest.mark.run(order=2)
def test_step2():
    print("2")
    assert 2 == 1

@pytest.mark.parametrize(("username","password"),[("zhangsan","zhangsan123"),("xiaoming","xiaoming123")])
def login_uu():
    pass

@pytest.mark.parametrize("name",["xiaoming","xiaohong"])
def one_user():
    pass

