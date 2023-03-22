from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('')

select = Select(driver.find_element(By.ID, 'selectA'))
select.select_by_visible_text('北京')

"""
selenium指定chrome.exe来发起请求如何实现？
地址：D:\work\Goole\Chrome\Application\chrome.exe
"""
path1 = r'D:\work\Goole\Chrome\Application\chrome.exe'
option = webdriver.ChromeOptions()
option.binary_location = path1
driver = webdriver.Chrome()

# driver.implicitly_wait(5)
