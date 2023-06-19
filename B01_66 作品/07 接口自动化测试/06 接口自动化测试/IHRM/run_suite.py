# 生成HTMLTestRunner测试报告
import unittest
from utils.HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
from testcases import test_login
from config import BASE_DIR
import time


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(test_login.TestLogin))


# 指定测试报告路径
report = BASE_DIR + "\\reports\\report_{}.html".format(time.strftime("%Y%m%d_%H%M%S"))
with open(report,'wb') as f:
    runner = HTMLTestRunner(stream=f, title="IHRM接口自动化测试报告")
    # 执行测试套件
    runner.run(suite)


