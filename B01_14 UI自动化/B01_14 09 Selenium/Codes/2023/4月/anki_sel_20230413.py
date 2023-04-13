from selenium import webdriver
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
zh = r'https://www.zhihu.com/signin?next=%2F'
driver = webdriver.Chrome()
driver.get(cdp)

# 将滚动条滑到最底层
js1 = "window.scrollTo(10000,10000)"
driver.execute_script(js1)
time.sleep(1)

driver.close()
