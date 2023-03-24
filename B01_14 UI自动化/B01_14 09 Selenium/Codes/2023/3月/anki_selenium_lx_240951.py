
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

cdp = r'D:\Program Files\pagetest\注册A.html'
zh = r'https://www.zhihu.com/signin?next=%2F'
option = webdriver.ChromeOptions()
option.binary_location = r'D:\work\Goole\Chrome\Application\chrome.exe'
driver = webdriver.Chrome
driver.get(cdp)

# 层级选择器：后代关系（不止父子）定位test1，然后写入值test1
e1 = driver.find_element(By.CSS_SELECTOR,'p[id="p1"]>input')
e1.send_keys('test1')

# 根据元素id属性来选择 id属性值为userA的元素
driver.find_element(By.ID, 'userA')

time.sleep(1)
driver.close()












