import unittest

class demo(unittest.TestCase):  # unittest测试类必须继承unittest.TestCase
    @classmethod  # 调用类方法
    def setUpclass(cls) -> None:  # setUp用来为测试准备环境，是自动运行的
        print("setup class")  # 运行在一开始

    @classmethod
    def tearDownClass(cls) -> None:  # teardown用来清理环境
        print("teardown class")  # 运行在最后
        
    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("testcase01")
        self.assertEqual(2, 2, "判断相等")
        self.assertIn('h', 'this')

    def test_case02(self):
        print("testcase02")
        self.assertEqual(1,1,"判断相等")

    @unittest.skipIf(1+1==2, "跳过这条用例")
    def test_case03(self):
        print("testcase03")
        self.assertEqual(3,4,"判断相等")

if __name__ == "__main__":
    unittest.main()