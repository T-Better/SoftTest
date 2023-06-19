from config import *
import json
import requests


# # 构造测试数据
# def build_data():
#     json_file = BASE_DIR + "/data/login.json"
#     ld = []
#     with open(json_file,encoding='utf-8') as f:
#         json_data = json.load(f)
#         for cd in json_data:
#             desc = cd['desc']
#             login_data = cd['login_data']
#             ld.append([desc, login_data])
#     return ld
#
# if __name__ == "__main__":
#     bd = build_data()
#     print(bd)


header1 = {"Content-Type":"application/json"}

def ihrm_login(login_data, url1):
    """login_data：入参"""
    res = requests.post(url=url1, json=login_data)
    # print(res)
    print(res.json())

if __name__ == "__main__":
    # 登录测试
    login_data = {
        "mobile": "13800000002",
        "password": "888itcast.CN764%..."
    }
    url1 = r'http://ihrm-java.itheima.net/api/sys/login'
    ihl = ihrm_login(login_data,url1)