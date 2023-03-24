from selenium import webdriver


driver= webdriver.Chrome()
driver.get('D:\Program Files\pagetest\{}'.format('注册A.html'))
"""
p2 = 'D:\work\Goole\Chrome\Application\chrome.exe'
option = webdriver.ChromeOptions()
option.binary_localtion = p2
"""
driver.maximize_window()  # 最大化浏览器
driver.get_cookies()

