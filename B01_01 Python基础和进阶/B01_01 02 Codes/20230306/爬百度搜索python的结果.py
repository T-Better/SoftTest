import requests


url = r'https://www.baidu.com/s'
kv = {"wd":"python"}
r = requests.get(url,params=kv)
print("写入成功")
with open(r'爬百度搜索python的结果.txt', mode='w') as f:
    f.write(r.text)








