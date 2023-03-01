import requests

def parse(url):
    r = requests.post(url)
    r.raise_for_status()
    return r.text

if __name__ == "__main__":
    # kv = {'key1':'value1'}
    url = r'http://python123.io/ws'
    # headers = {
    #     'User-Agent': 'MMozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0'
    # }
    data = parse(url)
    print(data)