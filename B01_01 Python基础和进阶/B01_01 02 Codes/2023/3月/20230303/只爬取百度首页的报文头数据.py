import requests


r = requests.head(r'http://www.baidu.com')
print(r.headers)



