from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# TODO

cdp = r'D:\Program Files\pagetest\注册A.html'
jp = r'C:\Users\Lenovo\Pictures\暂时'
driver = webdriver.Chrome() # chrome实例化
driver.get(cdp)  # 发起请求
e1 = driver.find_element(By.ID,'userA')

# selenium定位用户名输入框并输入制表符
e1.send_keys(Keys.TAB)

# 2). 截图保存
driver.get_screenshot_as_file('')



driver.close()










