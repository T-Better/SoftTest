import xml.etree.ElementTree as et
import requests
from bs4 import BeautifulSoup

url1 = r'http://python123.io/ws/demo.html'

r = requests.get(url1)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())



