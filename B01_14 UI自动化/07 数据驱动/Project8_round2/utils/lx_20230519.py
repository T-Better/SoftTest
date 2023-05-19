from selenium import webdriver
from selenium.webdriver.common.by import By

url1 = r"D:\Program Files\projectHtml\chapter8\index.html"
driver = webdriver.Firefox()
driver.get(url1)

driver.find_element(By.ID, 'ty-email').send_keys('admin@tynam.com')
driver.find_element(By.ID, 'ty-pwd').send_keys('tynam123')

login_btn = driver.find_element(By.CSS_SELECTOR,'[value="登  录"]')
login_btn.click()
alert1 = driver.switch_to.alert
# print(login_btn.driver.switch_to.alert().text)
print(alert1.text)
alert1.dismiss()

driver.close()
