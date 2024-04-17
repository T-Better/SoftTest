import requests
import pytest
from api.login import LoginApi



class TestLogin():
    # case1:登陆成功
    def __init__(self):
        self.login_api = LoginApi()
        self.session = requests.Session()

    def test_login_success(self):
        # 获取验证码
        response = self.login_api.get_login_verifycode(self.session)
        print("1")
        # 断言验证码返回的是不是图片
        assert response.header.get("Content-Type") == "image"
        print("2")
        # 登录



if __name__ == "__main__":
    pytest.main(['-s','-v','test_login.py'])
    # testlogin(login_url, data=login_data)