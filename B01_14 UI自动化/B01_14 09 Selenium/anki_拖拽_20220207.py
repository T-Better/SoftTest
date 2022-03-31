# anki_拖拽_20220207.py
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
action = ActionChains(driver)
driver.get(r'D:\Program Files\pagetest\drag.html')
red1 = driver.find_element_by_css_selector()
blue1 = 
action.drag_and_drop(red1,blue1).perform()


