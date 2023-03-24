# web_键鼠操作_20220129.py
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')

action = ActionChains(driver)





time.sleep(2)

driver.close()