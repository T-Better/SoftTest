# 获取验证码： http://localhost/index.php?m=Home&c=User&a=verify
# 登录 ： http://localhost/index.php?m=Home&c=User&a=do_login
# 导包
import requests
import unittest

# 创建测试类
class TPShopLogin(unittest.TestCase):
    def setUp(self):
        # 实例化session对象
        self.session = requests.Session()
        # 定义验证接口url地址
        self.url_verify = " http://localhost/index.php?m=Home&c=User&a=verify"
        # 定义登录接口url地址
        self.url_login = " http://localhost/index.php?m=Home&c=User&a=do_login"

    # teardown
    def tearDown(self):
        # 关闭session对象
        self.session.close()

    # 登录成功
    def test01_success(self):
        # 发送验证码请求并断言
        response = self.session.get(url=self.url_verify)
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发登录请求并断言
        login_data = {
            "username": "13488888888",
            "password": "123456",
            "verify_code": "8888"
        }
        response = self.session.post(url=self.url_login, data=login_data)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json().get("status"))
        self.assertIn("登陆成功", response.json().get("msg"))

    # 账号不存在
    def test02_user_is_not_exist(self):
        # 发送验证码请求并断言
        response = self.session.get(url=self.url_verify)
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发登录请求并断言
        login_data = {
        "username": "13488888899",
        "password": "123456",
        "verify_code": "8888"
        }
        response = self.session.post(url=self.url_login, data=login_data)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(-1, response.json().get("status"))
        self.assertIn("账号不存在", response.json().get("msg"))

    # 密码错误
    def test03_password_error(self):
        # 发送验证码请求并断言
        response = self.session.get(url=self.url_verify)
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发登录请求并断言
        login_data = {
        "username": "13488888888",
        "password": "error",
        "verify_code": "8888"
        }
        response = self.session.post(url=self.url_login, data=login_data)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(-2, response.json().get("status"))
        self.assertIn("密码错误", response.json().get("msg"))










