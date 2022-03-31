# test_复习20220208.py

import pytest

@pytest.mark.xfail(reason='1!=2')

def test_wish_fail():
    assert 1 == 2

@pytest.mark.run(order=1)
def test_step1():
    print("1")
    assert 1 == 1
@pytest.mark.parametrize('name',['xiaoming','xiaohong'])
@pytest.mark.run(order=4)
def test_step2():
    print("2")
    assert 2 == 1

# 使用fixture传递测试数据格式举例
@pytest.fixture
def test_a():
    return 1

@pytest.mark.parameterize(("username","password"),[("zhangsan","zhangsan123"),("xiaoming","xiaoming123")])
def test_b(test_a):
    assert 1 == test_a



