import json


class ReadConfig(object):
    """
    读取配置文件，Excel、json等文件的读取方法都可写在此类下
    """
    def __init__(self):
        pass
    def read_json(self,json_file):
        """
        读取Json文件
        用try-except来对错误进行对应说明：文件不存在或不是json文件
        :return: 返回字符串文件
        """
        try:
            with open(json_file) as f:
                data = json.load(f)
                return data
        except:
            print("文件不存在或不是json文件")

if __name__ == "__main__":
    data = ReadConfig().read_json("../config/base_data.json")  # 实例化类 调用其方法读取Json
    print(data)
    print(data['base_url'], data['email'],data['password'])  # 输出base_url email password的值 用来测试
