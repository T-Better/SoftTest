# selenium_name定位_注册A_20220117.py
import time
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome()

# 打开测试网站
driver.get('D:\Program Files\pagetest\注册A.html')

# 通过id定位到用户名输入框并在用户名输入框中输入admin
driver.find_element_by_name('userA').send_keys('admin')

# 通过id定位到密码输入框并在密码输入框中输入123456
driver.find_element_by_name('passwordA').send_keys('123456')

# 等待3秒
time.sleep(3)

# 推出浏览器驱动（释放系统资源）
driver.quit()
