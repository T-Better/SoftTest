import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')

e1 = driver.find_element(By.ID, 'userA')
e1.send_keys('admin')
time.sleep(3)
action = ActionChains(driver)
action.double_click(e1).perform()

driver.set_window_position(100,100)

driver.close()


