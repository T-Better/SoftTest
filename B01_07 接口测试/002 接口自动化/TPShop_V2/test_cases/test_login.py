import requests
import pytest
from api.login import LoginApi



class TestLogin():
    # case1:登陆成功
    def test_login_success(self):
        # 获取验证码
        response = self.login_api.get_login_verifycode(self.session)
        # 断言验证码返回的是不是图片
        assert("image",response.header.get("Content-Type"))

        # 登录



if __name__ == "__main__":
    login_api = LoginApi()
    pytest.main(['-s'])
    # testlogin(login_url, data=login_data)