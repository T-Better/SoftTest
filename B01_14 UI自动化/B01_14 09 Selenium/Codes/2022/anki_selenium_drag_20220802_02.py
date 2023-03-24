from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\drag.html')
red_box = driver.find_element(By.ID,'div1')
blue_box = driver.find_element(By.ID,'div2')
action = ActionChains(driver)
action.drag_and_drop(red_box,blue_box).perform()
time.sleep(1)
driver.close()











