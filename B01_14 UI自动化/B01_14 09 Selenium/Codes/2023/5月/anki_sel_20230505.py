from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


p = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Firefox()
driver.get(p)

action = ActionChains(driver)
e1 = driver.find_element(By.XPATH,'//p/button')
action.move_to_element(e1).perform()

# 回退（忽略跳过）键
# Keys.ESCAPE

# 获取title
# .title

# 删除一个字符，不是全部内容
# Keys.BACK_SPACE

# 代码实现隐式等待5秒
# .implicitly_wait(5)

# 获取页面上第一个超链接的地址
# e2 = driver.find_element(By.LINK_TEXT,'新浪')
# e2.get_attribute('href')

# 下图中的下拉框选到上海
e3 = driver.find_element(By.ID,'selectA')
select = Select(e3)
select.select_by_visible_text('上海')

# 2). 截图保存
driver.get_screenshot_as_file('')

time.sleep(2)

driver.close()
