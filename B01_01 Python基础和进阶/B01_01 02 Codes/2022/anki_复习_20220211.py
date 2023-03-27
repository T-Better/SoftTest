import requests
import yaml


url1 = 'http://www.baidu.com'
data1 = {"user-agent":"Chrome/10"}
r = requests.post(url1, headers=data1)
print(r.text)

data = {"s_data":{"test1":"hello1"},"sdata2":{"name":"newroman_1"}}
with open('data_20220211.yaml','w') as f:
    yaml.dump(data, f, encoding='utf8', allow_unicode = True)
