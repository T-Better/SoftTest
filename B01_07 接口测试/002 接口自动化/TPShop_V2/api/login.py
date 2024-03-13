import requests


class LoginApi():
    """
    封装登录接口
    把登录相关的东西都存到这里，后面可直接调取这里面的登录接口，而不需要每次都写请求、入参、地址
    session长链接
    """
    def __init__(self):
        # 带self
        self.login_url = r'http://localhost/index.php?m=Home&c=User&a=do_login'
        self.login_verifycode_url = r'http://localhost/index.php?m=Home&c=User&a=verify'

    def get_login_verifycode(self, session):
        return session.get(self.login_verifycode_url)

    def login(self,username,password,verify_code):
        login_data = {"username": username,"password": password,"verify_code": verify_code}
        return session.post(self.login_url, data=login_data)


if __name__ == "__main__":
    session = requests.Session()
    loginapi = LoginApi()
    vres = loginapi.get_login_verifycode(session)
    res = loginapi.login()
