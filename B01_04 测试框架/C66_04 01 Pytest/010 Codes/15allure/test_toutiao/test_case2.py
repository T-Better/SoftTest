from time import sleep
import pytest

@pytest.mark.parametrize('n', list(range(5)))
def test_no_fixture(login, n):
    sleep(1)
    print("==没有__init__测试用例，我进入头条了==", login)
