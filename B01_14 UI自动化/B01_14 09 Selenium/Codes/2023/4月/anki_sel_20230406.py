from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()

e1 = driver.find_element(By.ID,'userA')

# 回退（忽略跳过）键
e1.send_keys(Keys.ESCAPE)

# 将滚动条滑到最底层
js1 = "window.scrollTo(1000,1000)"
driver.execute_script(js1)

# 设置浏览器窗口位置 --> 设置浏览器位置:左上角
driver.set_window_position(0,0)

# 设置浏览器大小 设置浏览器宽、高(像素点300,300)
driver.set_window_size(300,300)





driver.close()

