import requests

url = r'https://detail.tmall.com/item.htm?id=659465187615'
try:
    r = requests.get(url)
    r.raise_for_status()
    data = r.text
    print(data)
except:
    print("爬取失败")



