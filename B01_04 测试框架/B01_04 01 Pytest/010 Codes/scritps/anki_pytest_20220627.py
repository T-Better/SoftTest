import allure

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass

@allure.severity('normal')
def test_case_5():
    """ 没标记 severity 的用例默认为 normal"""
    print("test case 5555555555")








