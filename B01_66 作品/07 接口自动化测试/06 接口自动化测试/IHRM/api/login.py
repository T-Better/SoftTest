# 带参数登录
import requests


class IhrmLogin(object):
    def __init__(self):
        self.url = r'http://ihrm-java.itheima.net/api/sys/login'


    def ihrm_login(self, login_data):
        """login_data：入参"""
        return requests.post(self.url, json=login_data)

if __name__ == "__main__":
    ihrml = IhrmLogin()
    print(ihrml.ihrm_login())