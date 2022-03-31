import pytest

@pytest.mark.parameterize(("user","password"),[("zhangsan","zhangsan123"),("xiaoming","xiaoming123")])
def test_i(self, name):
    print(name)
    assert 1
