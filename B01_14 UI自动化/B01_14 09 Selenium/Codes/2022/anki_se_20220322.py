from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
path1 = ''

driver = webdriver.Chrome()
e1 = WebDriverWait(driver,10,1).until(lambda x:x.find_element(By.ID,'userA'))
e1.send_keys('admin')










