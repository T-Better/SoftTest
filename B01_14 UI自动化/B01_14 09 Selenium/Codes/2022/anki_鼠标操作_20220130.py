# anki_鼠标操作_20220130.py
from selenium.webdriver.common.action_chains import ActionChains

action = ActionChains(driver)
action.move_to_element(e1)
action.double_click(e1)

js1 = "window_scrollTo(0,10000)"
driver.execute_script(js1)
action.perform()




