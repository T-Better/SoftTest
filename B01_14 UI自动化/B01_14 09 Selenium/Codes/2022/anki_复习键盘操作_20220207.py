# anki_复习键盘操作_20220207.py
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
e1 = driver.find_element_by_css_selector('[placeholder="请输入用户名"]')
# e1.send_keys(Keys.ESCAPE)
e1.send_keys('admin')
time.sleep(2)
action = ActionChains(driver)
action.double_click(e1).perform()
time.sleep(2)
# 空格
e1.send_keys(Keys.SPACE)
# 复制
e1.send_keys(Keys.CONTROL,'c')
# 制表符
e1.send_keys(Keys.TAB)
# 回车键
e1.send_keys(Keys.ENTER)
# 删除
e1.send_keys(Keys.BACK_SPACE)


driver.close()