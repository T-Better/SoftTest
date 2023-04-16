from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)

# 使用显式等待定位用户名输入框，如果元素存在，就输入admin
e1 = WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_id('userA'))
e1.send_keys('admin')

# 打开注册页面A，模拟鼠标悬停在‘注册’按钮上
action = ActionChains(driver)
action.move_to_element(e1).perform()

# 下拉框选到上海
select = Select(e1)
select.select_by_visible_text('bj')

driver.page_source
time.sleep(2)
driver.close()
