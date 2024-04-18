import requests
import pytest,os
from utils.get_data import build_data
from api.login import LoginApi
from parameterized import parameterized
from config import get_data_path


class TestLogin():
    def setup_class(self):
        self.login_api = LoginApi()
        self.session = requests.Session()

    login_json_path = get_data_path() + os.sep + 'login.json'
    @parameterized.expand(build_data(login_json_path))
    def test_login(self,desc,username,password,verify_code,status_code,status,msg):
        # 获取验证码
        response = self.login_api.login(username,password,verify_code)
        # 断言验证码返回的是不是图片
        print(desc)
        assert response.status_code == status_code
        print(msg)


if __name__ == "__main__":
    pytest.main(['-s','-v','test_login.py'])