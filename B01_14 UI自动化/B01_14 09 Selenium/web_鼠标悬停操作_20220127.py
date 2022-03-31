# web_鼠标悬停操作_20220127.py  我的代码
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
action = ActionChains(driver)
e1 = driver.find_element_by_xpath('//p/button')
action.move_to_element(e1).perform()
time.sleep(3)
driver.close()
