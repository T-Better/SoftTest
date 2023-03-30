from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)

# 层级选择器：后代关系（不止父子）定位test1，然后写入值test1
e1 = driver.find_element(By.CSS_SELECTOR,'p[id="p1"] input')
e1.send_keys('test1')
# selenium定位test1输入框并输入制表符
e1.clear()
e1.send_keys(Keys.TAB)

# 2). 截图保存
driver.get_screenshot_as_file('/')

# 获取页面上第一个超链接的地址
e2 = driver.find_element(By.LINK_TEXT, '新浪')
h2 = e2.get_attribute('href')
print(h2)

driver.close()
