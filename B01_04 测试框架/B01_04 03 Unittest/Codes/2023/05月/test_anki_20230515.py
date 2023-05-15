# a.py  参数化
import unittest
from parameterized import parameterized

# 求和
def my_sum(a, b):
    return a + b


class Testmy_sum(unittest.TestCase):
    # 把(1, 1, 2), (1, 0, 1), (0, 0, 0)中的三组值当做x、y、expect传进来计算
    @parameterized.expand([(1, 1, 2), (1, 0, 1), (0, 0, 0)])
    def test_01(self, x, y, expect):
        result = my_sum(x, y)
        self.assertEqual(result, expect)
