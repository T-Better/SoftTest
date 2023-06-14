"""
打开‘注册A.html’页面，完成以下操作
1). 填写注册用户名
2). 截图保存
"""
from selenium import webdriver
# TODO


cdp = r'D:\Program Files\pagetest\注册A.html'
jp = r'C:\Users\Lenovo\Pictures\暂时'
driver = webdriver.Chrome() # chrome实例化
driver.get(cdp)  # 发起请求

# 1). 填写注册用户名
e1 = ''.send_keys('amdin')

# 2). 截图保存
driver.get_screenshow_as_file('')


# 将滚动条滑到最底层
js1 = "window.scrollTo(1000,10000)"
driver.execute_script(js1)

driver.close()