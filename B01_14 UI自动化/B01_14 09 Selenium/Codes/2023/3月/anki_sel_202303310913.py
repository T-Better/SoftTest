from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)

# 获取页面上第一个超链接的地址
u1 = driver.find_element(By.LINK_TEXT,'新浪')
print(u1.get_attribute('href'))

# 设置浏览器窗口位置 --> 设置浏览器位置:左上角
driver.set_window_position(300,300)

# 空格
u1.send_keys(Keys.SPACE)

# 使用显式等待定位用户名输入框，如果元素存在，就输入admin
e1 = WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_id('userA'))

# 删除
e1.send_keys(Keys.BACK_SPACE)

# 回退（忽略跳过）键
e1.send_keys(Keys.ESCAPE)

# 设置浏览器大小 设置浏览器宽、高(像素点300,300)
driver.set_window_size(300,300)

# 将滚动条滑到最底层
js1 = "window.scrollTo(3000,3000)"
driver.execute_script(js1)

time.sleep(2)
driver.close()




