import yaml

data = {"s_data":{"test1":"hello1"},"sdata2":{"name":"newroman_1"}}
with open('./yamldata_20220407.yaml', 'w', encoding='utf8') as f:
    yaml.dump(data,f,encoding='utf8',allow_unicode=True)


