# anki_拖拽_202201291104.py
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\drag.html')
action = ActionChains(driver)

blue_s = driver.find_element_by_css_selector('[id="div1"]')
red_t = driver.find_element_by_css_selector('[id="div2"]')

# 打开注册页面A，在用户名文本框上点击鼠标右键

action.drag_and_drop(blue_s,red_t).perform()
time.sleep(2)
driver.close()
