import requests
from bs4 import BeautifulSoup
import yaml

url1 = r'http://python123.io/ws/demo.html'
res = requests.get(url1)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())



# 读取yaml
with open('../data_20220207.yaml', 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)




