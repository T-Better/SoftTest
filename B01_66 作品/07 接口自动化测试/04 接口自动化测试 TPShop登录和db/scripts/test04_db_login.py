# 1.导包
import requests
import unittest
from ..api.login import LoginAPI
from ..tools.dbutil import DBUtil
from parameterized import parameterized

# 构造数据
def build_data():
    # 获取数据库的数据
    sql = "select * from t_login"
    db_data = DBUtil.exe_sql(sql)
    test_data = []
    for case_data in db_data:
        username = case_data[2]
        password = case_data[3]
        verify_code = case_data[4]
        status_code = case_data[5]
        content_type = case_data[6]
        status = case_data[7]
        msg = case_data[8]
        test_data.append((username, password, verify_code, content_type, status_code, status, msg))
        print(test_data)
    return test_data


# 2.创建测试类
class TestLoginDb(unittest.TestCase):
    # 2.1 前置处理
    def setUp(self):
        self.login_api = LoginAPI()  # 实例化接口类
        self.session = requests.Session()  # 创建session对象

    # 2.2 后置处理
    def tearDown(self):
        if self.session:
            self.session.close()

    @parameterized.expand(build_data())
    # 2.3.创建测试用例
    def test01_login(self, username, password, verify_code, content_type, status_code, status, msg):
        # 调用验证码接口获取验证，并进行断言
        response = self.login_api.get_verify_code(self.session)
        self.assertEqual(status_code, response.status_code)
        self.assertIn(content_type, response.headers.get("Content-Type"))

        # 调用登录接口获取登录信息，并进行断言
        response = self.login_api.login(self.session, username, password, verify_code)
        print(response.json())
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(status, response.json().get("status"))
        self.assertIn(msg, response.json().get("msg"))

