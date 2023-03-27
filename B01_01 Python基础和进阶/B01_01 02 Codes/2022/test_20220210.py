import requests
import json


r = requests.get('http://www.baidu.com')
print('1')
body = r.json()
print(body)
