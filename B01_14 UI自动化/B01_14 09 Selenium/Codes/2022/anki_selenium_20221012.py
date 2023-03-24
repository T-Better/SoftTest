# 利用元素属性
# 需求：打开注册A.html页面，完成以下操作
# 1).利用元素的属性信息+标签定位用户名输入框，并输入：admin
# 2).仅利用元素的属性信息（不能有标签）精确定位密码输入框，并输入：123456
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

p1 = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(p1)

u1 = driver.find_element(By.XPATH,'//p/input[@id="userA"]')
u1.send_keys('admin')

p1 = driver.find_element(By.XPATH,'//*[@name="passwordA"]')
p1.send_keys('12345')
time.sleep(2)
# 代码实现隐式等待5秒
driver.implicitly_wait(3)
driver.close()
"""

# 添加cookie
"""
driver.add_cookie({'book1':"天龙八部"})
"""

# 根据option显示文本来定位（即通过图中北京等来定位）
"""
from selenium.webdriver.support.select import Select

select = Select(By.ID,'selecta')
select.select_by_visible_text('北京')
"""

# 打开注册A页面，完成以下操作
# 1).使用显式等待定位用户名输入框，如果元素存在，就输入admin
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get(r'D:\Program Files\pagetest\注册A.html')
element = WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_id('userA'))
element.send_keys('admin')
time.sleep(3)
driver.quit()


