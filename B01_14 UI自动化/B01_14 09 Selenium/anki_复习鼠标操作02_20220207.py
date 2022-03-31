# anki_复习鼠标操作_20220207.py
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
action = ActionChains(driver)
e1 = driver.find_element_by_css_selector('[placeholder="请输入用户名"]')
action.context_click(e1)
action.perform()

driver.close()
