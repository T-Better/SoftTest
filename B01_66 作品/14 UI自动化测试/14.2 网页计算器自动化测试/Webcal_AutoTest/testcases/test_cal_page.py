# V1 pytest版本
from utils.get_jsondata import get_jsondata
from utils.get_exceldata import *
from config import *
from pages.cal_page import CalElement
import pytest, allure
from loguru import logger
from utils.cal_testlog import trace


@allure.feature('网页计算器计算测试')
class TestCal():
    """
    计算测试 相当于业务层
    """
    @logger.catch
    # @pytest.mark.parametrize('a,b,expect', get_jsondata('caladd.json'))
    @pytest.mark.parametrize('a,b,expect', GetData().get_adddata())
    @allure.story('测试增加按钮，共4个case,3p1f')
    def test_add(self, a, b, expect):
        """
        expect:我们预期值
        res:实际计算结果
        """
        print(a, b, expect)
        cale = CalElement()
        add_res = cale.add(a,b)   # 进行计算
        assert add_res == str(expect)

    @logger.catch
    @allure.story('测试减按钮，共4个case,3p1f')
    # @pytest.mark.parametrize('a,b,expect',get_jsondata('calsubtract.json'))
    @pytest.mark.parametrize('a,b,expect', GetData().get_subdata())
    def test_subtract(self, a, b, expect):
        """测试减法"""
        subtract_res = CalElement().subtract(a,b)
        print(subtract_res)
        assert subtract_res == str(expect)

    @logger.catch
    @allure.story('测试乘法按钮，共4个case,3p1f')
    # @pytest.mark.parametrize('a,b,expect',get_jsondata('calmultiply.json'))
    @pytest.mark.parametrize('a,b,expect', GetData().get_muldata())
    def test_multiply(self, a, b, expect):
        """测试乘法"""
        multiply_res = CalElement().multiply(a, b)
        print(multiply_res)
        assert multiply_res == str(expect)

    @logger.catch
    @allure.story('测试除法按钮，共4个case,3p1f')
    # @pytest.mark.parametrize('a,b,expect', get_jsondata('caldevide.json'))
    @pytest.mark.parametrize('a,b,expect', GetData().get_devdata())
    def test_devide(self, a, b, expect):
        """测试除法"""
        devide_res = CalElement().devide(a, b)
        print(devide_res)
        assert devide_res == str(expect)


if __name__ == "__main__":
    # testcal = TestCal()
    # testcal.test_add()
    testfile = BASE_DIR + r'\testcases\test_cal_page.py'
    pytest.main(['-s', testfile,])
    # pytest -s ./testcases/test_cal_page.py --alluredir ./result/tmp  # 生成allure测试报告.json文件
    # allure serve ./result/tmp  # 根据报告.json文件生成可查看的在线测试报告














