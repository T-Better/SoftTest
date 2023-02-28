import yaml

data = {"s_data":{"test1":"hello1你好"},"sdata2":{"name":"newroman_1嘿嘿嘿"}}

with open('data3.yaml',mode='w',encoding='utf8') as f:
    yaml.dump(data,f,allow_unicode=True)




















