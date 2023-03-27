""""
get方式获取百度首页数据，提取其中的状态码、响应正文、编码方式、
从内容中分析出的响应内容编码方式和http响应内容的二进制
"""
import requests

url = 'https://www.baidu.com/s'
path = r'/SoftTest/Soft_test/SoftTest/B01_01 Python基础和进阶/B01_01 02 Codes/2023/3月/20230227'
fn = r'\百度搜索python结果_202302272022.html'

def baidu_python(url,fp,kv):
    try:
        r = requests.get(url,params=kv)
        r.raise_for_status()
        with open(fp,encoding='utf8',mode='w+') as f:
            f.write(r.text)
        print('请求成功')
    except:
        pass

if __name__ == "__main__":
    keyword = 'python'
    kv = {'wd':keyword}
    baidu_python(url,path+fn,keyword)
