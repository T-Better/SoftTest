import json
from config import *

def get_jsondata():
    """
    读取data下的json测试数据
    """
    data_path = BASE_DIR + r'/data/calculator.json'
    with open(data_path, 'r') as f:
        data = json.load(f)
    print(data)
    return data









