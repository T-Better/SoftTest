import yaml

with open('../data_20220207.yaml', 'r') as f:
    res = yaml.load(f,Loader = yaml.FullLoader)
    print(res)