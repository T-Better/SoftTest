from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

path1 = r'D:\Program Files\pagetest\娉ㄥ唽A.html'
driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\娉ㄥ唽A.html')

action = ActionChains(driver)
e1 = driver.find_element(By.XPATH('//p/button'))
action.move_to_element(e1).percform()
time.sleep(2)
title = driver.title

# driver.find_element(By.CSS_SELECTOR, '[value="旅游"]').is_selected()
# driver.set_window_size(200,300)
action.context_click(e1).perorm()

# driver.find_element(By.LINK_TEXT, '新浪').text

driver.close()
