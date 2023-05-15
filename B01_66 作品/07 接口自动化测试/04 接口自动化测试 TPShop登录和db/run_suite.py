import time
import unittest
import app
from tools.HTMLTestRunner import HTMLTestRunner
from scripts.test02_para_login import TestLoginAPI
from scripts.test04_db_login import TestLoginDb


# 封装测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLoginAPI))
suite.addTest(unittest.makeSuite(TestLoginDb))

# 指定测试报告路径
report = "{}/report/report-{}.html".format(app.BASE_DIR, time.strftime("%Y%m%d-%H%M%S"))

# 打开文件流
with open(report, 'wb') as f:
    # 创建HTMLTestRunner执行器
    runner = HTMLTestRunner(f, title="接口测试报告")

runner.run(suite)

