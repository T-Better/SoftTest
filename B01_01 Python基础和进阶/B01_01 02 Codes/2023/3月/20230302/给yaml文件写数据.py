import yaml

data = {"s_data":{"test1":"hello1"},"sdata2":{"name":"newroman_1"}}

with open('data3.yaml', mode='w') as f:
    yaml.dump(data,f,allow_unicode=True)



