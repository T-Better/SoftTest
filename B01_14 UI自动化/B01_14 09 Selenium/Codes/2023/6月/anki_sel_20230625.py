
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)

# 打开注册页面A，在用户名文本框上点击鼠标右键，注意需要两步
e1 = driver.find_element(By.ID,'userA')
time.sleep(2)
action = ActionChains(driver)
action.context_click(e1).perform()

# 设置浏览器大小 设置浏览器宽、高(像素点300,300)
driver.set_window_size(300,300)

driver.close()

