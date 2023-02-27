# 爬：百度搜索python的结果，url="https://www.baidu.com/s"
import requests

url = 'http://www.baidu.com/s'
keyword='python'
path = r'D:\Git_Reps\SoftTest\Soft_test\SoftTest\B01_01 Python基础和进阶\B01_01 02 Codes\20230227'
filename = r'\python_result_202302271958.txt'
try:
    kv = {'wd':keyword}
    r = requests.get(url,params=kv)
    r.raise_for_status()
    print(path+filename)
    with open(path+filename, encoding='utf8',mode = 'w+') as f:
        f.write(r.text)

except:
    print('爬取失败')


