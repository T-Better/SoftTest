# 浏览器控制_20220128.py
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# driver.get(r'D:\Program Files\pagetest\注册A.html')

# selenium如何自动修改某一项（如电话号码从0修改为1）
# driver.find_element_by_css_selector('[placeholder="请输入电话号码"]').send_keys('18600000000')
# time.sleep(2)
# driver.find_element_by_css_selector('[placeholder="请输入电话号码"]').clear()
# time.sleep(2)
# driver.find_element_by_css_selector('[placeholder="请输入电话号码"]').send_keys('18611111111')
# time.sleep(2)
# 刷新 
driver.refresh()

# 后退 
driver.back()

# 获取当前页面url 
driver.current_url()

# 最大化浏览器 
driver.maximize_window()

driver.forward()

# 设置浏览器大小 设置浏览器宽、高(像素点) 
driver.set_window_size(200,300)

# 设置浏览器窗口位置 --> 设置浏览器位置
driver.set_window_position(200,300)

# 获取title 
driver.title

# 获取用户名输入框的大小 
driver.find_element_by_css_selector('[placeholder="请输入用户名"]').size

# 获取页面上第一个超链接的文本内容
driver.find_element_by_link_text('新浪').text

# 获取页面上第一个超链接的地址
driver.find_element_by_link_text('新浪').get_attribute('href')

# 判断页面中取消按钮是否可用
driver.find_element_by_css_selector('[value="取消"]').is_enabled()

# 判断页面中的span标签是否可见
driver.find_element_by_css_selector('[name="sp1"]').is_displayed()




driver.close()