from selenium import webdriver
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
zh = r'https://www.zhihu.com/signin?next=%2F'
driver = webdriver.Chrome()
driver.get(zh)  # 打开知乎
time.sleep(1)

driver.get(cdp)  # 再去打开本地注册A
time.sleep(1)

driver.back()
time.sleep(1)

# 获取title


driver.close()











