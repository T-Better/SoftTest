from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import logging
import time

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
time.sleep(2)
js1 = "window.scrollTo(10000,10000)"
driver.execute_script(js1)

js2 = "window.scrollTo(0,10000)"
driver.execute_script(js2)

# 根据option显示文本来定位（即通过图中北京等来定位）
select = Select(driver.find_element_by_id(''))
select.select_element_by_visible_text()

alert = driver.switch_to.alert
alert.accept()


time.sleep(2)

driver.find_element(By.ID, '')
driver.find_element(By.XPATH,'')
driver.find_element(By.LINK_TEXT,'')
driver.find_element(By.NAME,'')
driver.find_element(By.TAG_NAME,'')
driver.find_element(By.CLASS_NAME,'')
driver.find_element(By.CSS_SELECTOR,'')

# python的日志模块包括哪些？顺序是什么？如何设置日志级别？
logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()
logging.basicConfig(level=logging.error)

# 打开注册页面A，模拟鼠标悬停在‘注册’按钮上
action = ActionChains(driver)
e1 = driver.find_element(By.XPATH, '//p/button')
action.move_to_element(e1).perform()

from selenium.webdriver.support.select import Select

select = Select(driver.find_element(By.XPATH))
select.select_by_value('北京')

driver.close()
