# web_鼠标双击操作_20220127.py 我的代码
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')

action = ActionChains(driver) # 实例化ActionChains对象

driver.find_element_by_css_selector(r'[placeholder="请输入用户名"]').send_keys('admin')
e1 = driver.find_element_by_css_selector(r'[placeholder="请输入用户名"]')
action.double_click(e1)  # 调用双击操作
action.perform()  # 执行

time.sleep(2)

driver.close()
