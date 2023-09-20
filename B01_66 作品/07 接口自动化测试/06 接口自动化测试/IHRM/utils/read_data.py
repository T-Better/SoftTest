from config import *
import json

class GetJsonData():
    """获取Json测试数据"""
    def get_jdata(self):
        """
        :return:
        """
        lcase = []  #
        with open(LOGIN_JDATA,encoding='utf-8') as f:
            jdata = json.load(f)
        for case in jdata:
            desc = case['desc']
            login_data = case['login_data']
            status_code = case['status_code']
            is_success = case['success']
            code = case['code']
            message = case['message']
            # lcase.append([desc,login_data,status_code,is_success,code,message])
            lcase.append([desc,login_data,status_code,is_success,code,message])
        return lcase


if __name__ == "__main__":
    gjd = GetJsonData()
    print(gjd.get_jdata())







