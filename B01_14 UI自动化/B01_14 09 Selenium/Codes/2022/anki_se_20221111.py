from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


p1 = r'D:\Program Files\pagetest'

"""
w1 = r'\drag.html'
wp1 = p1+w1

driver = webdriver.Chrome()
driver.get(wp1)
r1 = driver.find_element(By.ID,'div1')
b1 = driver.find_element(By.ID,'div2')
action = ActionChains(driver)
action.drag_and_drop(r1,b1).perform()
time.sleep(2)
"""

w2 = r'\注册A.html'
wp2 = p1+w2
driver = webdriver.Chrome()
driver.get(wp2)
"""
account = driver.find_element(By.CSS_SELECTOR,'.telA')
account.send_keys('admin')
time.sleep(3)
action = ActionChains(driver)
action.double_click(account).perform()
time.sleep(2)
"""

"""
action = ActionChains(driver)
log_up = driver.find_element(By.XPATH,'//p/button')
action.move_to_element(log_up).perform()
time.sleep(2)
"""

"""
l1 = driver.find_element(By.LINK_TEXT,'新浪')
print(l1.text)
"""



driver.close()














