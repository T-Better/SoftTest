import unittest
import requests
import json
from .. import app
from parameterized import parameterized
from ..api.login import LoginAPI
from ..utils import common_assert

# 构造测试数据
def build_data():
    json_file = app.BASE_DIR + "/data/login.json"
    ld = []
    with open(json_file,encoding='utf-8') as f:
        json_data = json.load(f)
        for cd in json_data:
            desc = cd('desc')
            login_data = cd('login_data')
            sc = cd('status_code')
            suc = cd('success')
            code = cd('code')
            msg = cd('message')
            ld.append((desc,login_data,sc,suc,code,msg))
    return ld

# 创建测试类
class TestLogin(unittest.TestCase):
    # 前置处理
    def setUp(self):
        self.login_api = LoginAPI()  # 登录api实例化
        # self.session = requests.Session()
        self.h1 = {"Content-Type":"application/json"}

    # 后置处理
    # def teardown(self):
        # self.session.close()

    # 定义测试用例
    # case 001 登陆成功
    @parameterized.expand(build_data)
    def test01_case001(self,desc,login_data,sc,suc,code,msg):
        response = self.login_api.login(login_data)
        print(response.json())

        # 断言
        common_assert(self, response)


