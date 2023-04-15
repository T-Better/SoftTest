import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import Alert

import logging

driver = webdriver.Chrome()
"""
driver.get(r'D:\Program Files\pagetest\drag.html')
action = ActionChains(driver)
# 打开‘drag.html’页面，把红色方框拖拽到蓝色方框上
p1 = driver.find_element(By.ID, 'div1')
p2 = driver.find_element(By.ID, 'div2')
action.drag_and_drop(p1, p2).perform()
time.sleep(2)
"""
# 粘贴 .send_keys(Keys.CONTROL,'v)
"""点击alert 获取并打印警告框文本 接受或忽略警告框 """
driver.find_element(By.XPATH, '//p/input[@type="button"]').click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
alert.dismiss()

logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()

logging.basicConfig(level=logging.ERROR)

# 将滚动条滑到最底层
js1 = "window.scrollTo(0,10000)"
driver.execute_script(js1)

# 根据option显示文本来定位（即通过图中北京等来定位）
from selenium.webdriver.support.select import Select
select = Select(driver.find_element(By.ID, 'selecta'))
select.select_by_visible_text('北京')

driver.close()
