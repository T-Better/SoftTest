# selenium定位test1输入框并输入制表符
from selenium import webdriver
# TODO
# TODO

cdp = r'D:\Program Files\pagetest\注册A.html'
jp = r'C:\Users\Lenovo\Pictures\暂时'
driver = webdriver.Chrome() # chrome实例化
driver.get(cdp)  # 发起请求


# selenium定位用户名输入框并输入制表符
# TODO

driver.close()