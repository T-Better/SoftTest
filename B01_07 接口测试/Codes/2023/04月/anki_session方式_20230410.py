# session方式
import requests

# 创建session对象
session = requests.Session()

# 获取验证码
url1 = r'http://localhost/index.php?m=Home&c=User&a=verify'  # 验证码地址
r = session.get(url=url1)

# 登录
login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {
"username": "13488888888",
"password": "123456",
"verify_code": "8888"
}
response =  session.post(url=login_url,data=login_data)
print(response)

# 我的订单：http://localhost/Home/Order/order_list.html
orurl = r'http://localhost/Home/Order/order_list.html'
response =  session.get(orurl)
print(response.text)
