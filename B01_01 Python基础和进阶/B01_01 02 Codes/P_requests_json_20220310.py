import requests
# 获取验证码
response = requests.get("http://localhost/index.php/Home/user/login.html")
print(response.cookies)
PHPSESSID = response.cookies.get("PHPSESSID")
print(PHPSESSID)
# 登录
login_url = "http://localhost/index.php/Home/user/login.html"
login_data = {
	"username": "13088888888",
	"password": "123456",
	"verify_code": "8888"
}
cookies = {"PHPSESSID": PHPSESSID}
response = requests.post(url=login_url, data=login_data, cookies=cookies)
print(response.json())
# 我的订单：http://localhost/Home/Order/order_list.html
response = requests.get("http://localhost/Home/Order/order_list.html",cookies=cookies)
print(response.text)