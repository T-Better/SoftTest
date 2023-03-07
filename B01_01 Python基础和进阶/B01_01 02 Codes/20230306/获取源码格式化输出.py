import requests
from bs4 import BeautifulSoup

url = r'http://python123.io/ws/demo.html'
r = requests.get(url)
s1 = BeautifulSoup(r.text,'html.parser')
print(s1.prettify())




