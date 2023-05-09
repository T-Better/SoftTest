# test01.py
# 导包
# 导包
import unittest


class my_test01(unittest.TestCase):
    # 写一个类级别fixture，包含setup teardown
    @classmethod
    def setUpClass(self):
        print("setUPClass 执行")

    @classmethod
    def tearDownClass(self):
        print("tearDownClass 执行")

    # 写一个函数级别fixture，包含setup teardown
    def setUp(self):
        print("setUP 执行")

    def tearDown(self):
        print("teardown 执行")
