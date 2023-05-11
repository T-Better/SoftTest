import requests

class LoginAPI:
    def __init__(self):
        # 初始化 增加url类属性
        self.url = r'http://ihrm-test.itheima.net/api/sys/login'

    # 定义接口调用方法
    def login(self,login_data):
        return requests.post(url=self.url, json = login_data)
