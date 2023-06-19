import pytest
from pages.cal_page import CalElement
# from config import *
from basepage.common.basepage import BasePage


@pytest.fixture(scope='session', autouse=True)
def cal_fixture():
    """
    开始测试前的准备：打开浏览器
    结束测试后的收尾：关闭浏览器
    """
    print('----------------------开始测试----------------------')
    calpage_obj = CalElement()
    yield
    print('----------------------结束测试----------------------')
    calpage_obj.driver.close()


# if __name__ == "__main__":
#     testfile = BASE_DIR + r'\testcases\test_cal_page.py'
#     pytest.main(['-s',testfile])












