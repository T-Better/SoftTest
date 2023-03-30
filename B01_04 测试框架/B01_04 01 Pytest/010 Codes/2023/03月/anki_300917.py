from collections import namedtuple
import pytest

# 如何用两种方法定义namedtuple对象User并赋值,如何对User赋默认值；
User = namedtuple('User','name,age,id')

User.__new__.__defaults__ = (None,None,False)
user = User('','','')
# 写一个典型（准备和收尾）的fixture，名为_tuple

@pytest.fixture
def a_tuple():
    # 1
    yield
    # 2

# pytest -s方法实现对test_file.py模块重跑5次；


# 实现 自动根据条件（tasks的版本如果小于0.2.0则跳过）判断是否要跳过test_unique_id_1案例
# @pytest.mark.skipif(tasks.__version__ < '',reason)

# 执行run.py后自动执行06conftest下所有的测试用例；
# pytest.main([-s,'../'])

# pytest如何控制函数执行的顺序的？如下两个如何先执行step1后执行step2?
@pytest.mark.run(order=2)
def test_step1():
    print("1")
    assert 1 == 1

@pytest.mark.run(order=4)
def test_step2():
    print("2")
    assert 2 == 1

# 数据参数化:name有多个时如何实现登录操作？
@pytest.parametrize('name',["","",""])
def p1(self, name):
    pass

# 如何只执行前三个操作（案例）？
@pytest.mark.n1
def ck_psw():
    pass
@pytest.mark.n1
def login():
    pass
@pytest.mark.n1
def logout():
    pass

def other():
    pass
# pytest -m n1

# 使用fixture传递测试数据格式举例
# a_tuple为fixture，传给test_a_tuple

def a_tuple():
    return 1

def test_a_tuple(a_tuple):
    assert a_tuple == 1


