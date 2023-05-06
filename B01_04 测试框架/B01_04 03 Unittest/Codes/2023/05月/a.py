# 定义一个实现加法操作的函数，并对该函数进行测试。
import unittest


def my_sum(a,b):
    return a + b

class my_test(unittest.TestCase):  # 新建测试类必须继承unittest.TestCase
    def test_01(self):
        print(my_sum(4,6))

    def test_02(self):
        print(my_sum(3, 2))

