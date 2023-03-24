import yaml

with open('data_20220113.yaml','r') as f:
    r = yaml.load(f,Loader=yaml.FullLoader)
    print(r)