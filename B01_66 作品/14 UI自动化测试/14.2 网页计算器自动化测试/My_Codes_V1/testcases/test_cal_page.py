# V1 pytest版本
from utils.get_jsondata import get_jsondata
from config import *
from pages.cal_page import CalElement
import pytest, allure

@allure.feature('网页计算器计算测试')
class TestCal():
    """
    计算测试 相当于业务层
    """
    @pytest.mark.parametrize('a,b,expect', get_jsondata('caladd.json'))
    @allure.story('测试增加按钮，共4个case')
    def test_add(self, a, b, expect):
        """
        expect:我们预期值
        res:实际计算结果
        """
        # print(a, b, expect)
        add_res = CalElement().add(a,b)   # 进行计算
        # print(add_res)
        assert add_res == str(expect)

    # @pytest.mark.parametrize('a,b,expect',get_jsondata('calsubtract.json'))
    # def test_subtract(self, a, b, expect):
    #     """测试减法"""
    #     subtract_res = CalElement().subtract(a,b)
    #     print(subtract_res)
    #     assert subtract_res == str(expect)
    #
    # @pytest.mark.parametrize('a,b,expect',get_jsondata('calmultiply.json'))
    # def test_multiply(self, a, b, expect):
    #     """测试乘法"""
    #     multiply_res = CalElement().multiply(a, b)
    #     print(multiply_res)
    #     assert multiply_res == str(expect)
    #
    # @pytest.mark.parametrize('a,b,expect', get_jsondata('caldevide.json'))
    # def test_devide(self, a, b, expect):
    #     """测试除法"""
    #     devide_res = CalElement().devide(a, b)
    #     print(devide_res)
    #     assert devide_res == str(expect)




if __name__ == "__main__":
    # testcal = TestCal()
    # testcal.test_add()
    testfile = BASE_DIR + r'\testcases\test_cal_page.py'
    pytest.main(['-s', testfile,])
    # pytest -s ./testcases/test_cal_page.py --alluredir ./report














