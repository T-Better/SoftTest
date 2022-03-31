from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
action = ActionChains(driver)

driver.find_element_by_css_selector('p[id="pa"]>input').send_keys('admin')
driver.find_element_by_css_selector('p[id="p1"] input').send_keys('......')

# 双击鼠标左键，选中admin
e1 = driver.find_element_by_css_selector('p[id="pa"]>input')
action.double_click(e1)
action.perform()

time.sleep(2)
driver.quit
