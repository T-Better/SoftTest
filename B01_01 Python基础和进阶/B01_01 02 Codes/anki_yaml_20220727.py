import yaml

p1 = r'./data_20220118.yaml'

with open(p1,'r') as f:
    data = yaml.load(f,Loader=yaml.FullLoader)
print(data)