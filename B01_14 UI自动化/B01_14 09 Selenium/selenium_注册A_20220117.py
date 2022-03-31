# 注册A_20220117.py
import time
from selenium import webdriver

# 创建浏览器对象
driver = webdriver.Chrome()

# 打开测试网站
driver.get('D:\Program Files\pagetest\注册A.html')

# 通过id定位用户名输入框并在用户名输入框中输入admin
driver.find_element_by_id('userA').send_keys('admin')

# 通过id定位到密码输入框并在密码输入框中输入123456
driver.find_element_by_id('passwordA').send_keys('123456')

# 等待3s
time.sleep(3)

# 退出浏览器
driver.quit()

