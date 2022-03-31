import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
e2 = WebDriverWait(driver, 10,1).until(lambda x:x.find_element_by_id('userA'))
e1 = driver.find_element(By.ID, 'fw')
print(e1.get_attribute('href'))

driver.implicitly_wait(5)
driver.find_element(By.id,'').send_keys(Keys.CONTROL,'c')

# 截图
driver.get_screenshot_as_file('./img/image_20220314.png')
a1 = driver.find_element(By.ID,'alerta')
alert = driver.switch_to.alert

print(alert.text)
alert.dismiss()
alert.accept()

from selenium.webdriver.support.wait import WebDriverWait

e3 = WebDriverWait(driver, 3, 1).until(lambda x:x.find_element(By.ID, ''))
driver.get_screenshot_as_file('./img/image_000.png')

e3.send_keys(Keys.CONTROL, 'a')

driver.quit()


