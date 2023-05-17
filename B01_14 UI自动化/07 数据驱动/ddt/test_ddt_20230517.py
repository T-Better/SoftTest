from ddt import ddt,data,unpack
import unittest
import time

@ddt
class MyTesting(unittest.TestCase):
    def setUp(self):
        print("-- 开始测试 --")
        time.sleep(1)
    def tearDown(self):
        print("-- 结束测试 --")
        time.sleep(1)

    # @data('hello','world')
    # def test_print(self, value):
    #     print("传入的值是：" + value)

    @data([3,2,5],[3,2,4])
    @unpack
    def test_add(self, a, b, expected):
        actual = int(a) + int(b)
        excepted = int(expected)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()


