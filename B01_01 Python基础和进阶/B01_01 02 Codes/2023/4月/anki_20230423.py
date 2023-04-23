"""
打开‘注册A.html’页面，完成以下操作
1). 填写注册用户名
2). 截图保存
"""
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
zh = r'https://www.zhihu.com/signin?next=%2F'
driver = webdriver.Chrome()
driver.get(cdp)

# 将滚动条滑到最底层
js1 = "window.scrollTo(1000,1000)"
driver.execute_script(js1)

driver.implicitly_wait(5)

# 最大化浏览器
driver.maximize_window()

# 使用显式等待定位用户名输入框，如果元素存在，就输入admin
e1 = WebDriverWait(driver,10,1).until(lambda a:driver.find_element_by_id('userA'))

# 模拟鼠标悬停在‘注册’按钮上
action = ActionChains(driver)
action.move_to_element(e1).perform()

# 根据option显示文本来定位
select = Select(e1)
select.select_by_visible_text('上海')

# cookie
driver.get_cookie('cookiename')

driver.close()









