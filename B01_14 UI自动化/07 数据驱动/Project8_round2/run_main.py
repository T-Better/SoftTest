"""
使用HTMLTestRunner执行测试并生成HTML类型测试报告
created on 2023-05-18
project:TYNAM后台管理系统
@Author:TYnam
"""

import os, time, unittest
from HTMLTestRunner import HTMLTestRunner
from app import BASE_DIR


# 获取当前路径
report_path = BASE_DIR + r"\report"
# 获取当前时间
now = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))

# 标题
title = u"TYNAME后台管理系统"

# 设置报告存放路径，并且以当前时间进行报告命名
report_abspath = os.path.join(report_path, title + now + ".html")

def all_case():
    """ 导入所有的用例 """
    case_path = os.getcwd()
    discover = unittest.defaultTestLoader.discover(case_path, pattern="Test*.py")

    print(discover)
    return discover

if __name__ == "__main__":
    fp = open(report_abspath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title = title)
    runner.run(all_case())
    fp.close()








