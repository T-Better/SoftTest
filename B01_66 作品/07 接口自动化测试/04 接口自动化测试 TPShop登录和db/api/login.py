# 封装被测系统接口
import requests

# 定义接口类
class LoginAPI():
    # 初始化
    def __init__(self):
        self.url_verify = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.url_login = "http://localhost/index.php?m=Home&c=User&a=do_login"
        self.session = requests.Session()
        # 获取验证码接口
    def get_verify_code(self, session):
        vc = session.get(url = self.url_verify)
        return vc

    # 登录接口
    def login(self, session, username, password, verify_code):
        login_data = {
            "username": username,
            "password": password,
            "verify_code": verify_code
        }
        r1 = session.post(self.url_login, data = login_data)
        return r1


















