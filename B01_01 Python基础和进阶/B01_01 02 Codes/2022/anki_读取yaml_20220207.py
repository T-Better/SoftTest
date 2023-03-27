# anki_读取yaml_20220207.py
import yaml

with open(r'D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66 02 Python基础和进阶/data_20220207.yaml') as f:
    res = yaml.load(f,Loader = yaml.FullLoader)
    print(res)

