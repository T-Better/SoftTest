import requests
from bs4 import BeautifulSoup


def parse_sc(url):
    """
    获取源码 输出text
    """
    r = requests.get(url)
    r.raise_for_status()
    return r.text

def fc(sc):
    """
    格式化源码
    """
    soup = BeautifulSoup(sc,'html.parser')
    scf = soup.prettify()
    return scf


if __name__ == "__main__":
    url = r'http://python123.io/ws/demo.html'
    ct = parse_sc(url)
    scf = fc(ct)
    print(scf)