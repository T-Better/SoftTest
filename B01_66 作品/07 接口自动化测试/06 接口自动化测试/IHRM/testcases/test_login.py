# unittest方法
import unittest
from api.login import IhrmLogin
from parameterized import parameterized
from utils.read_data import GetJsonData
from utils.utils import common_assert


class TestLogin(unittest.TestCase):
    # 前置处理
    def setUp(self):
        self.login_api = IhrmLogin()  # login api实例化
        self.h1 = {"Content-Type": "application/json"}
        # self.login_data = GetJsonData()

    def tearDown(self):
        pass

    # 定义测试用例
    @parameterized.expand(GetJsonData().get_jdata())
    def test01_login(self, desc, login_data, sc, suc, code, msg):
        login_res = self.login_api.ihrm_login(login_data)
        # print(login_res)
        # print(login_res.json())
        # print(login_res.json().get('success'))
        # print(login_res.json().get('code'))
        # print(login_res.json().get('message'))
        # print("---------------------------------")
        # 断言
        common_assert(self, login_res)


if __name__ == "__main__":
    tl = TestLogin()
    tl.test01_login()





