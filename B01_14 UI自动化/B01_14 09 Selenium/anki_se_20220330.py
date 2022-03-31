from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time
p1 = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(p1)
e1 = driver.find_element(By.XPATH,'//p/button')
action = ActionChains(driver)
action.move_to_element(e1)
time.sleep(2)



driver.close()
