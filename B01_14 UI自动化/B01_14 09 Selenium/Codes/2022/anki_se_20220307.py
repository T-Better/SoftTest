from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

p1 = r'D:\Program Files\pagetest\drag.html'
driver = webdriver.Chrome()
driver.get(p1)
action = ActionChains(driver)
red_box = driver.find_element(By.ID, "div1")
blue_box = driver.find_element(By.ID, "div2")

action.drag_and_drop(red_box, blue_box).perform()
time.sleep(2)


driver.close()






