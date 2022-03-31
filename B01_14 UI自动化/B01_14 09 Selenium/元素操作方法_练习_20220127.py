# 元素操作方法_练习_20220127.py 我的代码
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
"""
1).通过脚本执行输入用户名：admin；密码：123456；电话号码：18611111111；
电子邮件：123@qq.com 
"""
driver.find_element_by_xpath('//p[@id="pa"]/input').send_keys('admin')
driver.find_element_by_css_selector('[placeholder="请输入密码"]').send_keys('123456')
driver.find_element_by_css_selector('.telA').send_keys('18611111111')
driver.find_element_by_xpath('//p/input[@placeholder="请输入电子邮箱"]').send_keys('123@qq.com')

# 间隔3秒，修改电话号码为：18600000000
time.sleep(3)
driver.find_element_by_css_selector('.telA').clear()
driver.find_element_by_css_selector('.telA').send_keys('18600000000')

# 3).间隔3秒，点击‘注册’按钮 
time.sleep(3)
driver.find_element_by_xpath('//p/button').click()
time.sleep(2)

# 4).间隔3秒，关闭浏览器 
driver.quit()
