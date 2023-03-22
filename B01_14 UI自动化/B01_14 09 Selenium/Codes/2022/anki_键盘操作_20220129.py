# anki_键盘操作_20220129.py
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')

e1 = driver.find_element_by_css_selector('[placeholder="请输入用户名"]')

e1.send_keys(Keys.ENTER)


