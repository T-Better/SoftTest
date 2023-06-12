# 打开‘drag.html’页面，把红色方框拖拽到蓝色方框上
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)

e1 = driver.find_element(By.ID, 'div1')
e2 = driver.find_element(By.ID, 'div2')
action = ActionChains(driver)
action.drag_and_drop(e1,e2).perform()
# time.sleep(1)

driver.close()
