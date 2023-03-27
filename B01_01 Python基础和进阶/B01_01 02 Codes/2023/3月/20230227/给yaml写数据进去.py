import yaml

path = r'/SoftTest/Soft_test/SoftTest/B01_01 Python基础和进阶/B01_01 02 Codes/2023/3月/20230227'

data = {"s_data":{"test1":"hello1"},"sdata2":{"name":"newroman_1"}}

with open('data_3.yaml', mode='w') as f:
    yaml.dump(data,f,encoding='urf8',allow_unicode=True)









