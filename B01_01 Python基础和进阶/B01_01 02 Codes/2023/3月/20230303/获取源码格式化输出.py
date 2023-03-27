import requests
from bs4 import BeautifulSoup


def parse(url):
    r = requests.get(url)
    r.raise_for_status()
    return r.text


def fc(c):
    sc = BeautifulSoup(c, 'html.parser')
    return sc.prettify()


if __name__ == "__main__":
    url = r'http://python123.io/ws/demo.html'
    c = parse(url)
    print(fc(c))





