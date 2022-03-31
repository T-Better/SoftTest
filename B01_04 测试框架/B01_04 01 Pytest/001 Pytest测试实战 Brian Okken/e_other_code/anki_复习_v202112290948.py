import pytest
from collections import namedtuple
from Task import tasks

@pytest.mark.skipif(tasks.__version__ < '0.2.0',reason='1')
@pytest.mark.xfail
def test_unique_id_1():
    pass

@pytest.mark.check_pwd
def check_password():
    pass

User = namedtuple('User','name,age,genter')
User.__new__.__default__ = (None,None,False)
user = User('lisi','18','1')

@pytest.fixture
def a_tuple():
    assert 1 == 2  # fixture中的assert
    return 1

def test_a_tuple(a_tuple):
    assert a_tuple == 2  # 
