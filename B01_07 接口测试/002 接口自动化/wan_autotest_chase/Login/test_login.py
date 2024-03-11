import requests

login_url = r'https://www.wanandroid.com/user/login'
login_data = {"username":"TBetter","password":"Wanandroid3016_"}
r1 = requests.post(login_url,json=login_data)
print(r1.status_code)


