# 打开注册页面A，模拟鼠标悬停在‘注册’按钮上
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


path1 = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(path1)
# e1 = driver.find_element_by_id('userA')

# action = ActionChains(driver)
# action.move_to_element(e1)

"""
打开注册A.html页面，完成以下操作
1).利用元素的属性信息+标签定位用户名输入框，并输入：admin
2).仅利用元素的属性信息（不能有标签）精确定位密码输入框，并输入：123456
"""
driver.find_element(By.XPATH, '//p/input[@placeholder="请输入用户名"]').send_keys('admin')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@placeholder="请输入密码"]').send_keys('123456')
time.sleep(2)
driver.close()