# 将 test01.py、test02.py 2 条用例批量执行；
import unittest
import test01
import test02

suite = unittest.TestSuite()
suite.addTest(test01.my_test01('test_01'))
suite.addTest(unittest.makeSuite(test02.my_test02))

runner = unittest.TextTestRunner()
runner.run(suite)

