import yaml

data = {"s_data":{"test1":"hello1"},"sdata2":{"name":"newroman_1"}}
with open('','w') as f:
    yaml.dump(data, f, encoding='UTF8', allow_unicode=True)





