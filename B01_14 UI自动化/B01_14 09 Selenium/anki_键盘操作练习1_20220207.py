# anki_键盘操作练习1_20220207.py
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')

e1 = driver.find_element_by_css_selector('[placeholder="请输入用户名"]')
e1.send_keys('admin1')
time.sleep(2)
e1.send_keys(Keys.BACK_SPACE)  # 删除1
e1.send_keys(Keys.CONTROL,'a')  # 全选用户名：admin
e1.send_keys(Keys.CONTROL,'c')  # 复制用户名：admin
e2 = driver.find_element_by_css_selector('[placeholder="请输入密码"]')
e2.send_keys(Keys.CONTROL,'v')
time.sleep(2)
driver.close()
