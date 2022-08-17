from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
action = ActionChains(driver)
e1 = driver.find_element(By.CSS_SELECTOR,'placeholder="请输入用户名"')
action.context_click(e1)
time.sleep(2)
action.perform()
time.sleep()
# 设置浏览器大小 设置浏览器宽、高(像素点)
driver.set_window_size(300,300)
#1). 填写注册信息
driver.find_element(By.CSS_SELECTOR,'placeholder="请输入用户名"').send_keys('请输入用户名')
# 2). 截图保存
driver.get_screensht_as_file('./book.png')

#打开注册页面A，模拟鼠标悬停在‘注册’按钮上
action.move_to_element(e1).perform()
# 获取页面上第一个超链接的地址
link1 = driver.find_element_by_link_text('访问 新浪 网站').get_attribute('href')
# 调用：接受对话框选项
# alert.accept()
# send_keys(Keys.ESCAPE)
driver.close()






