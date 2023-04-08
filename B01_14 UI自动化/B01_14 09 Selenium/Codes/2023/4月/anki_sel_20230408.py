from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)

# 使用显式等待定位用户名输入框，如果元素存在，就输入admin
e1 = WebDriverWait(driver, 10, 1).until(lambda x:x.find_element_by_id('userA'))
e1.send_keys('admin')

# 打开注册页面A，模拟鼠标悬停在‘注册’按钮上
e2 = driver.find_element(By.XPATH,'//p/button')
action = ActionChains(driver)
action.move_to_element(e2).perform()

# 根据option显示文本来定位
e3 = driver.find_element(By.ID,'selectA')
select = Select(e3)
# select.select_by_value('sh')
select.select_by_visible_text('上海')

# 代码实现隐式等待5秒，说明其含义
driver.implicitly_wait(5)

time.sleep(2)
driver.close()










