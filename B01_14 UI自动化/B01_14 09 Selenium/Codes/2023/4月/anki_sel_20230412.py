from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)
e1 = ''
# 打开注册页面A，在用户名文本框上点击鼠标右键，注意需要两步
action = ActionChains(driver)
action.context_click(e1).perform()
time.sleep(2)

driver.close()