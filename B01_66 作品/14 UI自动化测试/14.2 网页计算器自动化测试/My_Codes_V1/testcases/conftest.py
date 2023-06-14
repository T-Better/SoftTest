import pytest
# from pages.cal_page import CalElement
# from config import *
# from basepage.common.basepage import BasePage


@pytest.fixture(scope='class')
def cal_fixture():
    """
    开始测试前的准备：打开浏览器
    结束测试后的收尾：关闭浏览器
    """
    # CALURL = r'http://cal.apple886.com/'
    print('----------------------开始测试----------------------')
    # basepageobj = BasePage()
    # basepageobj.open_page(CALURL)
    # basepageobj.driver.get(CALURL)
    # basepageobj.driver.maximize_window()
    # calpageobj = CalElement()
    # print('----------------------setup----------------------')
    yield
    # basepageobj.driver.close()
    print('----------------------teardown----------------------')

# if __name__ == "__main__":
#     testfile = BASE_DIR + r'\testcases\test_cal_page.py'
#     pytest.main(['-s',testfile])












