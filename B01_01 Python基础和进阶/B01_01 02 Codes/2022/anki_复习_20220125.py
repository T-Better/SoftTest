# 爬虫：如何只获取百度首页的请求头
import requests

url = ''
json1 = {"key1":"value1"}
r = requests.pody(url,json=json1)
print(r.text)
