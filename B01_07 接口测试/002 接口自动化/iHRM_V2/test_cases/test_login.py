import requests
# import pytest

login_url = r'http://192.168.146.130:8080/wx/auth/login'
login_data = {
    "username": "test10000",
    "password": "123456"
}
def testlogin(url,data):
    login_res = requests.post(url,data)
    assert login_res.status_code == 200


if __name__ == "__main__":
    # pytest.main(['-s'])
    testlogin(login_url, data=login_data)