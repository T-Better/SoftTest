# session方式登录
import requests

# 创建session对象
session = requests.Session()

# 获取验证码 get
url1 = r'http://localhost/index.php?m=Home&c=User&a=verify'  # 验证码地址
rc = session.get(url1)

# 登录 post
login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

response =  session.post(login_url)
print(response)

# 我的订单get：http://localhost/Home/Order/order_list.html
orurl = r'http://localhost/Home/Order/order_list.html'
# response =  # TODO
print(response.text)
