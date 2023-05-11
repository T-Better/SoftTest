import unittest
from scripts import test01_login
from tools.HTMLTestRunner import HTMLTestRunner
import time
import app

# 封装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(test01_login.TestLogin))

# 指定测试报告路径
report = app.BASE_DIR + "/report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
with open(report,'wb') as f:
    runner = HTMLTestRunner(stream = f, title="IHRM接口测试报告")

runner.run(suite)
