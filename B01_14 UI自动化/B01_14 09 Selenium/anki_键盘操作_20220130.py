# anki_键盘操作_20220130.py
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
"""
# 1). 输入用户名：admin1，暂停2秒，删除1
driver.find_element_by_css_selector('[placeholder="请输入用户名"]').send_keys('admin1')
time.sleep(2)
e1 = driver.find_element_by_css_selector('[placeholder="请输入用户名"]')
e1.send_keys(Keys.BACK_SPACE)
# 2). 全选用户名：admin，暂停2秒
e1.send_keys(Keys.CONTROL,'a')
time.sleep(2)
# 3). 复制用户名：admin，暂停2秒
e1.send_keys(Keys.CONTROL,'c')
# 4). 粘贴到密码框
driver.find_element_by_css_selector('[placeholder="请输入密码"]').send_keys(Keys.CONTROL,'v')
time.sleep(2)
driver.close()
"""
