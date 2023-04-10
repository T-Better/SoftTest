"""
1. 请求IHRM项目的登录接口，URL： http://localhost/index.php?m=Home&c=User&a=do_login
2. 请求头： Content-Type: application/json
3. 请求体： {"mobile":"13088888888", "password":"123456"}
"""
import requests
login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
h1 = {'Content-Type':'application/json'}
ld =  {"mobile":"13088888888", "password":"123456"}
# 发送请求
response = requests.post(url=login_url, data=ld,headers=h1)
# 查看响应
print(response.text)
