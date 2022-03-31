import pytest

@pytest.fixture()
def pwd():
    print("获取密码")
    a = "polo"
    return a


def test_2(pwd):
    raise NameError
    assert pwd == "polo"


