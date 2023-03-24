
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

cdp = r'D:\Program Files\pagetest\注册A.html'
zh = r'https://www.zhihu.com/signin?next=%2F'
driver = webdriver.Chrome()
driver.get(cdp)

# 层级选择器：后代关系（不止父子）定位test1，然后写入值test1
driver.find_element(By.CSS_SELECTOR,'p[id="p1"]>input').send_keys('test1')

time.sleep(1)
driver.close()












