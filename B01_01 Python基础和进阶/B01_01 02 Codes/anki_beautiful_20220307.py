import requests
from bs4 import BeautifulSoup
url1 = 'http://python123.io/ws/demo.html'

r = requests.get(url1)
soup1 = BeautifulSoup(r.text, 'html.parser')
print(soup1.prettify())

