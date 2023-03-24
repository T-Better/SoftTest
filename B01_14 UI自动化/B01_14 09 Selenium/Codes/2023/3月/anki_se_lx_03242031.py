from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)

# 1).使用id定位，输入用户名：admin
"""
driver.find_element(By.ID,'userA').send_keys('admin')
"""

# 2).使用id定位，输入密码：123456
"""
driver.find_element(By.ID, 'passwordA').send_keys('123456')
"""

# 使用显式等待定位用户名输入框，如果元素存在，就输入admin
"""
e1 = WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_id('userA'))
e1.send_keys('admin')
"""

"""
e1 = driver.find_element(By.ID,'selectA')
select = Select(e1)  # 实例化select
select.select_by_visible_text('广州') 
"""

time.sleep(2)
driver.close()

