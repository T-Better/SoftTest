from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("")
e = WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_id("userA"))
e.send_keys("admin")
time.sleep(3)
driver.quit()

