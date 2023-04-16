"""
1. 请求IHRM项目的登录接口，URL： http://localhost/index.php?m=Home&c=User&a=do_login
2. 请求头： Content-Type: application/json
3. 请求体： {"mobile":"13088888888", "password":"123456"}
"""
import requests
login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
d={"mobile":"13088888888", "password":"123456"}
h={'Content-Type': 'application/json'}
# 发送请求
response = requests.post(url=login_url,data=d,headers=h)
# 查看响应
print(response.text)
