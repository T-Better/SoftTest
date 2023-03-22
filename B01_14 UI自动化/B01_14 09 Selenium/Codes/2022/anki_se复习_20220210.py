import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
action = ActionChains(driver)  # action实例化
e1 = driver.find_element_by_xpath('//p/button')
action.move_to_element(e1)
action.perform()
time.sleep(2)
driver.close()





