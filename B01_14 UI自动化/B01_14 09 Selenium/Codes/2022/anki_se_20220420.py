from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# 根据option显示文本来定位（即通过图中北京等来定位）
driver = webdriver.Chrome()
driver.get('')
select = Select(driver.find_element(By.ID,'selectA'))
select.select_by_visible_text('北京')

# 将滚动条滑到最底层
js1 = "Window.scrollTo(6000,6000)"
driver.execute_script(js1)

# 获取当前页面url
url = driver.current_url

"""
selenium指定chrome.exe来发起请求如何实现？
地址：D:\work\Goole\Chrome\Application\chrome.exe
"""
option = webdriver.ChromeOptions()
option.binary_location = r''
driver = webdriver.Chrome()

