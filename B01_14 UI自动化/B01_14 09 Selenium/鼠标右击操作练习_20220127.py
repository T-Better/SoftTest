# 鼠标右击操作练习_20220127.py 我的代码
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
action = ActionChains(driver)  # 实例化ActionChains对象

e1 = driver.find_element_by_css_selector('[placeholder="请输入用户名"]')
action.context_click(e1)  # 调用右键方法

action.perform()
time.sleep(2)
driver.close()