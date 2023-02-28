import yaml

with open('data3.yaml',mode='r',encoding='utf8') as f:
    data = yaml.load(f,Loader = yaml.FullLoader)
print(data)


