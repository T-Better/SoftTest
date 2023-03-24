from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

driver = webdriver.Chrome()
WebDriverWait(driver, 2, 1).until(lambda x:x.find_element_by_id("userA"))


driver.quit()





