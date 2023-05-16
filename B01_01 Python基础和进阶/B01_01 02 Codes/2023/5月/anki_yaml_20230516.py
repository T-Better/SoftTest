import yaml

data = {"s_data":{"test1":"hello1"},"sdata2":{"name":"newroman_1"}}
with open('./data_3.yaml','w') as f:
    yaml.dump(data,f,encodging="utf-8",allow_unicode=True)
