import requests
from bs4 import BeautifulSoup

r = requests.get('http://python123.io/ws/demo.html')
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

