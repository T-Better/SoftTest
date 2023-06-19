# 带参数登录
import requests


class IhrmLogin(object):
    def __init__(self):
        self.url = r'http://ihrm-java.itheima.net/#/login'

    def ihrm_login(self, login_data):
        """login_data：入参"""
        return requests.get(self.url, data=login_data)

if __name__ == "__main__":
    ihrml = IhrmLogin()
    print(ihrml.ihrm_login())