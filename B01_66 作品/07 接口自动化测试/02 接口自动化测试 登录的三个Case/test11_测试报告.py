import unittest
import time
from test10_unittest_tpshop import TPShopLogin
from test12_unittest_参数化 import TPShopLogin2
from HTMLTestRunner import HTMLTestRunner


# 封装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TPShopLogin))  # 测试TPShopLogin中的所有case 成功 不存在 错误
suite.addTest(unittest.makeSuite(TPShopLogin2))  # 测试TPShopLogin2中的所有case
# suite.addTest(TPShopLogin2('test01_login'))

# 指定测试报告路径
rp = r"./report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

# 打开文件流
with open(rp, mode = 'wb') as f:
    runner = HTMLTestRunner(f, title = 'tpshop接口测试报告')

    # 执行测试套件
    runner.run(suite)
