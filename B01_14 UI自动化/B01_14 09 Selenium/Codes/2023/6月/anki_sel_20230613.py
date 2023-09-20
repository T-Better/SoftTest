
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

cdp = r'D:\Program Files\pagetest\注册A.html'
zh = r'https://www.zhihu.com/signin?next=%2F'
driver = webdriver.Chrome()
driver.get(zh)

# 获取title
t = driver.title
print(t)

# 使用显式等待定位用户名输入框，如果元素存在，就输入admin
WebDriverWait(10,1,driver).until(lambda x:x.find_element(By.ID,''))

driver.close()







