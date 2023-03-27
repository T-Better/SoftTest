import yaml

with open('../data_20220207.yaml', encoding='utf8') as f:
    data = yaml.load(f,Loader=yaml.FullLoader)
print(data)



