import requests

url="https://www.baidu.com/s"
kv = {'wd':'python'}
r = requests.get(url,params = kv)
print(r.text)

