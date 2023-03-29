from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)

e1 = driver.find_element(By.ID,'selectA')

# 根据option显示文本来定位
"""
select = Select(e1)
select.select_by_visible_text('上海')
"""

# 使用显式等待定位用户名输入框，如果元素存在，就输入admin
e2 = WebDriverWait(driver, 10,1).until(lambda x:x.find_element_by_id('userA'))

# 粘贴
e1.send_keys(Keys.CONTROL,'V')

# 刷新
driver.refresh()

# 获取当前页面url
u1 = driver.current_url

# 获取页面上第一个超链接的文本内容
u1 = driver.find_element(By.LINK_TEXT, '新浪').text

# 最大化浏览器
driver.maximize_window()

t1 = driver.page_source

# 模拟鼠标悬停在‘注册’按钮上
action = ActionChains(driver)
action.move_to_element(e1).perform()

# 隐式等待5秒
driver.implicitly_wait(5)

# 删除
e1.send_keys(Keys.BACK_SPACE)

time.sleep(2)
driver.close()
