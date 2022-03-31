import pytest
import time

@pytest.mark.parametrize("n", list(range(5)))
def test_get_info(login, n):
    time.sleep(1)
    name, token = login
    print("***基础用例：获取用户个人信息***", n)  # Todo：这个n是有啥作用？
    print(f"用户名:{name}, token:{token}")


