import allure
import pytest
import os

@allure.feature('test_success')
def test_success():
    """this test succeeds"""
    assert True

@allure.feature('test_failure')
def test_failure():
    """this test fails"""
    assert False

@allure.feature('test_skip')
def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')

@allure.feature('test_broken')
def test_broken():
    raise Exception('oops')

if __name__ == '__main__':
    # pytest.main(["-s","allure-test.py"])
    '''
    -q: 安静模式, 不输出环境信息
    -v: 丰富信息模式, 输出更详细的用例执行信息
    -s: 显示程序中的print/logging输出
    '''
    pytest.main(['-s', '-q','test_allure6_202202241535.py','--clean-alluredir','--alluredir=allure-results'])
    os.system(r"allure generate -c -o allure-report")
