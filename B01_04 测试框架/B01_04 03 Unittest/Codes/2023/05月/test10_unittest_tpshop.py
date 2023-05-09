# 导包
import unittest
import requests


# 创建测试类
class TPShopLogin(unittest.TestCse):
    pass

    # 创建测试方法
    # setup
    def setup(self):
        # 实例化session对象
        self.session = requests.Session()
        # 定义验证接口url地址
        self.url_verify = r'http://localhost/index.php?m=Home&c=User&a=verify'
        # 定义登录接口url地址
        self.url_login = r'http://localhost/index.php?m=Home&c=User&a=do_login'

    # teardown
    def teardown(self):
        # 关闭session对象
        self.session.close()

    # 登录成功
    def test01_success(self):
        self.rd = {"username": "13488888888", "password": "123456", "verify_code": "8888"}
        # 发送验证码请求并断言
        rc = self.session.get(url=self.url_verify)
        self.assertEqual(200, rc.status_code)  # 判断验证码是否是200，是的话继续，不是则退出

        # 发登录请求并断言
        r = self.session.post(url=self.url_login, data=self.rd)
        print(r.json())
        self.assertEqual(200, r.status_code)
        self.assertIn('登陆成功', r.json().get('msg'))

        # 账号不存在

    def test02_user_is_not_exist(self):
        # 发送验证码请求并断言
        r2d = {"username": "13488888889", "password": "123456", "verify_code": "8888"}
        # 发登录请求并断言
        r2 = self.session.get(url=self.url_verify, data=self.r2d)
        self.assertEqual(200, r2.status_code)
        self.assertIn('不存在', r2.json().get('msg'))

    # 密码错误
    def test03_password_error(self):
        # 发送验证码请求并断言
        r3c = self.session.get(url=self.url_verify)
        self.assertEqual(200, r3c.status_code)
        # 发登录请求并断言
        r3d = {
            "username": "13488888888",
            "password": "error",
            "verify_code": "8888"
        }
        r3 = self.session.post(url=self.url_login, data=r3d)
        self.assertEqual(200, r3.status_code)
        self.assertIn('密码错误', r3.json().get('msg'))
