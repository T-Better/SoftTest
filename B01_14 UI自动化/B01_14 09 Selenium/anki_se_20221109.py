from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
driver.find_element(By.ID,"alerta").click()
alert = driver.switch_to.alert
at1 = alert.text
print(at1)
alert.accept()
# alert.dismiss()

driver.close()



















