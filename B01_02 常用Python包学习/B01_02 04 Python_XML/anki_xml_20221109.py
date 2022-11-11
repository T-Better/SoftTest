import requests
from bs4 import BeautifulSoup

url1 = r'http://python123.io/ws/demo.html'
r1 = requests.get(url1)
soup = BeautifulSoup(r1.text,'html.parser')
print(soup.prettify())



