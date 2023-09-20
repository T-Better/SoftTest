# unittest和Pytest方法
import unittest, pytest, allure
from parameterized import parameterized
from utils.read_data import GetJsonData
from utils.utils import common_assert
from api.login import IhrmLogin
from utils.ihrm_autotest_log import trace
from loguru import logger


# class TestLogin(unittest.TestCase):
    # # 前置处理  unittest使用
    # def setUp(self):
    #     self.login_api = IhrmLogin()  # login api实例化
    #     self.h1 = {"Content-Type": "application/json"}
    #     # self.login_data = GetJsonData()
    #
    # def tearDown(self):
    #     pass

class TestLogin():
    # 定义测试用例
    # @parameterized.expand(GetJsonData().get_jdata())  # 数据驱动 方法一
    @logger.catch
    @allure.title("测试登录接口 预期12pass 1fail")
    @pytest.mark.parametrize("desc, login_data, sc, suc, code, msg", GetJsonData().get_jdata())  # 数据驱动 方法二
    def test01_login(self, desc, login_data, sc, suc, code, msg):
        login_api = IhrmLogin()
        login_res = login_api.ihrm_login(login_data)
        # 断言
        # common_assert(self, login_res)  # unittest专用
        assert sc == login_res.status_code
        assert suc == login_res.json().get("success")
        assert code == login_res.json().get("code")
        assert msg in login_res.json().get("message")


if __name__ == "__main__":
    tl = TestLogin()
    tl.test01_login()
    # pytest -s ./testcases/test_login.py --alluredir ./result/tmp  # 生成allure测试报告.json文件
    # allure serve ./result/tmp  # 根据报告.json文件生成可查看的在线测试报告




