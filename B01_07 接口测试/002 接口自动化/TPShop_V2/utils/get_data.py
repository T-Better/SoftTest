import json
import os
from config import get_data_path


def build_data(data_path):
    # 先读取Json吧，后面改成读yaml
    with open(data_path,encoding='utf-8') as f:
        logindata = json.load(f)
        test_data = []
        for ca in logindata:
            desc = ca.get('desc')
            username = ca.get('username')
            password = ca.get('password')
            verify_code = ca.get('verify_code')
            status_code = ca.get('status_code')
            status = ca.get('status')
            msg = ca.get('msg')
            test_data.append([desc, username, password,verify_code,status_code,status,msg])
    return test_data


if __name__ == "__main__":
    # testlogin(login_url, data=login_data)
    login_json_path = get_data_path() + os.sep + 'login.json'
    build_data(login_json_path)


