from bs4 import BeautifulSoup
import requests

url1 = r'http://python123.io/ws/demo.html'
r = requests.get(url1)
bs1 = BeautifulSoup(r.text,'html.parser')
print(bs1.prettify())







