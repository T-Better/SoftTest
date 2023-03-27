# anki_python_20220208.py
import requests
url = 'https://detail.tmall.com/item.htm?id=659465187615'
r = requests.get(url)
print(r.text())



