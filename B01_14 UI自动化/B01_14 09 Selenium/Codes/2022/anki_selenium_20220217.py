import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
# alert = driver.switch_to.Alert()
# 调用：取消对话框选项
# alert.dismiss()

e1 = driver.find_element(By.CSS_SELECTOR, '')
e1.send_keys(Keys.CONTROL, 'a')
action = ActionChains(driver)
# 双击鼠标左键，选中admin
action.double_click(e1)

driver.close()


