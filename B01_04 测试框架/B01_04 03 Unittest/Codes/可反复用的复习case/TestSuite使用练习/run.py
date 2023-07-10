# 将 test01.py、test02.py 2 条用例批量执行；
# 生成 HTMLTestRunner 测试报告
# 实现使用TestSuite方法将 test01.py中的my_test01类的test_01方法、test02.py中所有test开头的方法用例批量执行；
# TODO
import unittest
import test01,test02

suite = unittest.TestSuite()
suite.addTest(test01.my_test01('test_01'))
suite.addTest(unittest.makeSuite(test02.my_test02))

runner = unittest.TextTestRunner()
runner.run(suite)

