import unittest
from test.pages.loginPage import LoginPage



class TestLogin(unittest.TestCase):
    """登陆测试"""

    @classmethod
    def setUpClass(cls):
        cls.login = LoginPage()

    @classmethod
    def tearDownClass(cls):
        cls.login.quit_driver()

    def test_login01(self):
        """登陆成功"""
        self.login.login()

if __name__ == "__main__":
    unittest.main()







