"""
需求：
1. 请求TPshop项目的登录接口，请求数据（username: 13088888888, password: 123456,
verify_code: 1234）
2. 登录接口URL：http://localhost/index.php?m=Home&c=User&a=do_login
"""
import requests

url = r'http://127.0.0.1/index.php/Home/user/login.html'
login_data = {
    "username": "13088888888",
    "password": "123456",
    "verify_code": "8888"
}
r = requests.post(url = url, data = login_data)

print(r.text)










