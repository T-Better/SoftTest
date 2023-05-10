# 获取验证码： http://localhost/index.php?m=Home&c=User&a=verify
# 登录 ： http://localhost/index.php?m=Home&c=User&a=do_login
# 导包
import unittest
import requests
import json
from parameterized import parameterized


# 构造测试数据
def build_data():
    test_data = []
    file = './data/login.json'
    with open(file, encoding = 'utf-8') as f:
        json_data = json.load(f)
        for case_data in json_data:
            username = case_data.get('username')
            password = case_data.get('password')
            verify_code = case_data.get('verify_code')
            status_code = case_data.get('status_code')
            status = case_data.get('status')
            msg = case_data.get('msg')
            test_data.append((username,password,verify_code,status_code,status,msg))
    print("test_data=".format(username, password, verify_code, status_code,status, msg))
    return test_data

# 创建测试类
class TPShopLogin2(unittest.TestCase):
    def setUp(self):
        # 实例化session对象
        self.session = requests.Session()
        # 定义验证接口地址
        self.url_verify = " http://localhost/index.php?m=Home&c=User&a=verify"
        # 定义登录接口url
        self.url_login = " http://localhost/index.php?m=Home&c=User&a=do_login"

    def tearDown(self):
        self.session.close()

    # 登陆成功
    @parameterized.expand(build_data)
    def test01_login(self, username, password, verify_code, status_code, status, msg):
        # 发送验证码请求并断言
        response = self.session.get(url=self.url_verify)
        self.assertEqual(200,response.status_code)
        # self.assertIn('image', response.headers.get("Content-Type"))
        # print('1')
        # 发登陆请求并断言
        login_data = {
            "username":username,
            "password":password,
            "verify_code":verify_code
        }
        res2 = self.session.post(url=self.url_login, data = login_data)
        # print('2')
        print(response)
        self.assertEqual(status_code, res2.status_code)
        self.assertEqual(status, res2.json().get('status'))
        self.assertIn(msg, res2.json().get('msg'))




