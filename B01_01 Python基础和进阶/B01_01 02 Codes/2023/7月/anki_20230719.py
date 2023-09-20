from bs4 import BeautifulSoup
import requests

h1 = r'http://python123.io/ws/demo.html'

r1 = requests.get(h1)
s1 = BeautifulSoup(r1.text,'html.parser')
print(s1.prettify())










