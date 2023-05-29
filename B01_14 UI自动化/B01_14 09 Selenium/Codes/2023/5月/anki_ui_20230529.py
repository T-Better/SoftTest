
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)

# 使用显式等待定位用户名输入框，如果元素存在，就输入admin
e1 = WebDriverWait(driver,10,1).until(lambda x:x.find_element(By.ID,'userA'))
e1.send_keys('admin')

time.sleep(2)
driver.close()












