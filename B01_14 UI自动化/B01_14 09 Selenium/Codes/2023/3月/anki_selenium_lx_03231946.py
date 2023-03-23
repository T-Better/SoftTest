from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

cdp = r'D:\Program Files\pagetest\注册A.html'
zh = r'https://www.zhihu.com/signin?next=%2F'
driver = webdriver.Chrome()
driver.get(cdp)

# 通过元素的后代关系（不止父子）定位test1
driver.find_element(By.CSS_SELECTOR,'p[id="p1"] input').send_keys('test1')


# 输入空格
"""
driver.get(cdp).send_keys(Keys.SPACE)
"""

# 设置浏览器大小 设置浏览器宽、高(像素点)
# TODO
"""
driver.set_window_size(500,500)
time.sleep(1)
"""

# 将滚动条滑到最底层
# todo
# time.sleep(1)

# 退回知乎
"""
driver.get(zh)  # 打开知乎
time.sleep(1)

driver.get(cdp)  # 再去打开本地注册A
time.sleep(1)

driver.back() # 退回知乎
time.sleep(1)
"""

# 获取title
"""
t = driver.title
print(t)
"""

# 判断页面中'旅游'对应的复选框是否为选中的状态
# TODO

# 获取指定cookie
"""
c1 = driver.get_cookies()
print(c1)
"""

# 打开注册页面A，在用户名文本框上点击鼠标右键，注意需要两步
"""
ac = driver.find_element(By.CSS_SELECTOR, '[name="userA"]')
action = ActionChains(driver)  # 鼠标事件链实例化
action.context_click(ac)  # 右键
action.perform()  # 右键执行
time.sleep(2)
"""


time.sleep(1)
driver.close()
