import unittest
from scripts import test01_login, test02_employee
from tools.HTMLTestRunner import HTMLTestRunner
import time
import app

# 封装测试套件
suite = unittest.TestSuite()
# 登录接口测试用例
suite.addTest(unittest.makeSuite(test01_login.TestLogin))
# 员工管理场景用例
suite.addTest(test01_login.TestLogin("test01_case001"))
suite.addTest(unittest.makeSuite(test02_employee.TestEmployee))

# 指定测试报告路径
report = app.BASE_DIR + "/report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
with open(report,'wb') as f:
    runner = HTMLTestRunner(stream = f, title="IHRM接口测试报告")

# 执行测试套件
runner.run(suite)
