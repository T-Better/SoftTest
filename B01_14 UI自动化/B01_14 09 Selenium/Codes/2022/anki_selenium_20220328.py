"""
打开注册A页面，完成以下操作
1).使用显式等待定位用户名输入框，如果元素存在，就输入admin
"""
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


f1 = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(f1)
e1 = WebDriverWait(driver,2,1).until(lambda x:x.driver.find_element(By.ID, 'userA'))
e1.send_keys('admin')

# 2). 截图保存
e1.get_screenshot_as_file('r1.png')

# 在用户名文本框上点击鼠标右键，注意需要两步
action = ActionChains(driver)
action.context_click(e1).perform()

# 获取页面上第一个超链接的地址
driver.find_element(By.LINK_TEXT,'新浪').get_attribute('href')

# 后退
driver.back()

# 将日志信息输出到文件中
import logging
logging.basicConfig(filename='./log/20220328.log')

driver.close()
