# 需求：
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

cdp = r'D:\Program Files\pagetest\注册A.html'
jp = r'C:\Users\Lenovo\Pictures\暂时'
driver = webdriver.Chrome() # chrome实例化
driver.get(cdp)  # 发起请求

# 1). 填写注册用户名
driver.find_element(By.ID, 'userA').send_keys('111111')

# 2). 截图保存
driver.get_screenshot_as_file(jp+r'\202303222045.jpg')

# selenium定位用户名输入框并输入制表符
driver.find_element(By.ID,'userA').send_keys(Keys.TAB)

# 设置浏览器窗口位置 --> 设置浏览器位置:左上角
driver.set_window_position(0,0)

# 1).使用CSS定位方式中id选择器定位用户名输入框，并输入：admin
# TODO

# 2).使用CSS定位方式中属性选择器定位密码输入框，并输入：123456
# TODO
# 3).使用CSS定位方式中class选择器定位电话号码输入框，并输入：18600000000

# 4).使用CSS定位方式中元素选择器定位注册按钮，并点击

time.sleep(1)

driver.close()
