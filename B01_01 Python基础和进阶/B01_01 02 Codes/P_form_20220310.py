import requests

login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {
    "username": "13088888888",
    "password": "123456",
    "verify_code": "8888"
}
response = requests.post(url=login_url, data=login_data)

print(response.json())

