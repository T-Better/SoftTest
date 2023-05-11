
# session方式登录
import requests

# 创建session对象
session = requests.Session()

# 获取验证码 get
url1 = r'http://localhost/index.php?m=Home&c=User&a=verify'  # 验证码地址
r = session.get(url1)

# 登录 post
login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {
    "username": "13488888888",
    "password": "123456",
    "verify_code": "8888"
    }
response = session.post(login_url,data = login_data)
print(response)

# 我的订单get：http://localhost/Home/Order/order_list.html
url = r'http://localhost/Home/Order/order_list.html'
response = session.get(url)
print(response.text)