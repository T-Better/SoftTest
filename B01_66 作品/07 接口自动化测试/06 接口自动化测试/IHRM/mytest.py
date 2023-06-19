from config import *
import json


# 构造测试数据
def build_data():
    json_file = BASE_DIR + "/data/login.json"
    ld = []
    with open(json_file,encoding='utf-8') as f:
        json_data = json.load(f)
        for cd in json_data:
            login_data = cd['login_data']
            ld.append([login_data])
    return ld

if __name__ == "__main__":
    bd = build_data()
    print(bd)

# d1 =  {
#       "mobile": "13800000002",
#       "password": "888itcast.CN764%..."
#     }
#
# l2 = []
#
# l2.append(d1)
# print(l2)