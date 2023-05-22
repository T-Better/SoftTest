from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
f1 = r'D:\Program Files\projectHtml\chapter9\period4-1\index.html'
driver.get(f1)

e1 = driver.find_element(By.CSS_SELECTOR,'.tabs')
print(e1)

driver.close()
