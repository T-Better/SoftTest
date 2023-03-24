# anki_复习鼠标操作_20220207.py
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
action = ActionChains(driver)

# 模拟鼠标悬停在‘注册’按钮上
e1 = driver.find_element_by_xpath('//p/button')
action.move_to_element(e1)
action.perform()



driver.close()
