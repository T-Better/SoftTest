import allure
import pytest

@allure.attach('a.txt',allure.attachment_type.TEXT)
def attach_file_in_module_scope_fixture_with_finalizer(request):
    pass

# allure：命令行参数方式(pytest -v...)只运行test_severity.py中缺陷等级为blocker、critical的测试用例，并生成测试报告到allure文件夹中
# pytest -v test_severity.py --allure-severities=blocker,critical --alluredir=./allure

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass

def test_case_5():
    """ 没标记 severity 的用例默认为 normal"""
    print("test case 5555555555")
