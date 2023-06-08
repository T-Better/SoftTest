import json
from config import *

def get_jsondata(name):
    """
    读取data下的json测试数据
    """
    data_path = BASE_DIR + r'/data/{}'.format(name)
    with open(data_path, 'r') as f:
        data = json.load(f)
    print(data)
    print(data_path)
    return data

if __name__ == "__main__":
    get_jsondata('caladd.json')








