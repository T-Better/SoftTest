import requests


def parse(url,header):
    '''
    带头post爬数据
    '''
    r = requests.get(url,headers = header)
    r.raise_for_status()
    return r.text

if __name__ == "__main__":
    url = r'http://www.baidu.com'
    header = {'user-agent': 'Chrome/10'}
    print(parse(url,header))





