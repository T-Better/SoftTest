from basepage.common.basepage import BasePage
from selenium.webdriver.common.by import By


# 对象库层
class CalElement(BasePage):
    """
    封装各种元素对象：清屏、加、减、乘、除、等于
    """

    def clear_ele(self):
        """计算器清屏"""
        return self.driver.find_element(By.ID,'simpleClearAllBtn')

    def add_ele(self):
        """计算 加"""
        return self.driver.find_element(By.ID, 'simpleAdd')

    def subtract_ele(self):
        """计算 减"""
        return self.driver.find_element(By.ID, 'simpleSubtr')

    def multiply_ele(self):
        """计算 乘"""
        return self.driver.find_element(By.ID, 'simpleMulti')

    def devide_ele(self):
        """计算 除"""
        return self.driver.find_element(By.ID, 'simpleDivi')

    def equal_ele(self):
        """计算 等于"""
        return self.driver.find_element(By.ID, 'simpleEqual')

    def get_result(self):
        """计算 结果"""
        res = self.driver.find_element(By.ID,'resultIpt').get_attribute('value')
        print(res)
        return res

    # def digit_btn(self):
    #     """数字按钮"""
    #     return self.driver.find_element(By.ID, 'simple{}')

    def find_digit_btn(self, num):
        """定位数字按钮"""
        return self.driver.find_element(self.digit_btn[0], self.digit_btn[1].format(num))

# class Oper_Ele():
#     """
#     元素操作
#     """
#     def click_add(self):
#         """点击加按钮"""
#         pass
#
#     def click_subtract(self):
#         """点击减按钮"""
#         pass
#
#     def click_multiply(self):
#         """点击乘按钮"""
#         pass
#
#     def click_devide(self):
#         """点击除按钮"""
#         pass
#
#     def click_clear(self):
#         """点击清屏"""
#         pass
#
#     def click_digit(self):
#         """点击数字"""
#         pass
#
#     def

# class Cal_Scene():
#     """计算场景 加减乘除"""
    def add(self, a, b):
        """加"""
        self.find_digit_btn(a).click()
        self.add_ele().click()
        self.find_digit_btn(b).click()
        self.equal_ele().click()
        return self.get_result()

    def subtract(self,a,b):
        """减"""
        self.find_digit_btn(a).click()
        self.devide_ele().click()
        self.equal_ele().click()
        return self.get_result()

    def multiply(self,a,b):
        """乘"""
        self.find_digit_btn(a).click()
        self.multiply_ele().click()
        self.equal_ele().click()
        return self.get_result()

    def devide(self,a,b):
        """除"""
        self.find_digit_btn(a).click()
        self.devide_ele().click()
        self.equal_ele().click()
        return self.get_result()

if __name__ == "__main__":
    cal = CalElement()
    cal.get_result()
    # print("执行成功")









