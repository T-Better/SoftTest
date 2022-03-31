"""
打开注册A.html页面，完成以下操作
1).使用link_text定位(访问 新浪 网站)超链接，并点击
2).3秒后关闭浏览器窗口
"""
import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('D:\Program Files\pagetest\注册A.html')

driver.find_element_by_link_text('访问 新浪 网站').click()

time.sleep(3)

driver.quit()
