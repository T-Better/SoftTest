from collections import namedtuple
import pytest

User = namedtuple('User','name,age,id')
User.__new__.__defaults__ = (None,None,False)

user = User('张三','18','09')

print(user)

class TestLogin:
    @pytest.mark.parametrize(
        ("username","password"),[("zhangsan","zhangsan123"),("xiaoming","xiaoming123")]
    )
    def test_a(self):
        pass






