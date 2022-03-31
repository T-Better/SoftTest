# web键盘操作练习_20220128.py 我的代码
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')

# 1). 输入用户名：admin1，暂停2秒，删除1 
username = driver.find_element_by_id('userA').send_keys('admin1')
time.sleep(2)

username = driver.find_element_by_id('userA')
username.send_keys(Keys.BACK_SPACE)
time.sleep(2)

# 2). 全选用户名：admin，暂停2秒 
username.send_keys(Keys.CONTROL,'a')
time.sleep(2)

# 3). 复制用户名：admin，暂停2秒 
username.send_keys(Keys.CONTROL,'c')
time.sleep(2)

# 4).将用户名粘贴到密码中
password1 = driver.find_element_by_css_selector('[placeholder="请输入密码"]')
password1.send_keys(Keys.CONTROL,'v')
time.sleep(2)

driver.close()
