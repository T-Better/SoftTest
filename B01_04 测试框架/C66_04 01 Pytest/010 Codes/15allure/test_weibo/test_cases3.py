from time import sleep
import pytest

@pytest.mark.parametrize('n', list(range(5)))
class TestWeibo:
    def test_case1_01(self, open_weibo, n):
        sleep(1)
        print("查看微博热搜", n)

    def test_case1_02(self, open_weibo, n):
        sleep(1)
        print("查看微博范冰冰", n)

