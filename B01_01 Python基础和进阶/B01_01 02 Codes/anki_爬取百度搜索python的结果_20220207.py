# anki_爬取百度搜索python的结果_20220207.py
import requests

url="https://www.baidu.com/s"
kw1 = {"wd":'python'}
r = requests.get(url,params = kw1)
print(r.text)

