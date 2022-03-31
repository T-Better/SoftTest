from selenium.webdriver.support.select import Select
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
"""
driver.find_element_by_css_selector('[id="alerta"]').click()

# 获取并打印警告框文本
alert = driver.switch_to.alert  # 获取警告框文本
time.sleep(1)
print(alert.text)  # 打印警告框文本
time.sleep(1)
# 接受或忽略警告框
alert.accept()
# alert.dismiss()
time.sleep(1)
"""
# 根据option显示文本来定位
select = Select(driver)
select.select_by_visible_text('北京')

# 将滚动条滑到最顶层
js2 = "window.scorllTo(0,0)"
driver.execute_script(js2)

# 刷新
driver.refresh()
# 最大化浏览器 
driver.maximize_window()
# 获取title 
driver.title
#设置浏览器窗口位置 --> 设置浏览器位置
driver.set_window_position(200,100)
# 设置浏览器大小 设置浏览器宽、高(像素点) 
driver.set_window_size(200,100)

driver.close()
