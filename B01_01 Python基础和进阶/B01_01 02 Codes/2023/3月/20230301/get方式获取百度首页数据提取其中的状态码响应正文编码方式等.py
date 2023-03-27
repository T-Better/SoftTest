"""
get方式获取百度首页数据，提取其中的状态码、响应正文、编码方式、从内容中分析出的响应内容编码方式和http响应内容的二进制
易忘：从内容中分析出的响应内容编码方式和http响应内容的二进制
注意：做到捕获异常和根据状态码是否是200决定是否继续还是抛错
"""
import requests

url = r'https://www.baidu.com'
r = requests.get(url)
print("状态码：{}".format(r.status_code))
print("编码方式：{}".format(r.encoding))
print("内容中分析出的响应内容编码方式:{}".format(r.apparent_encoding))






