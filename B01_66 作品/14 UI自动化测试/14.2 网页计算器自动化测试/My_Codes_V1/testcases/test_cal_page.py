# V1 pytest版本
from utils.get_jsondata import get_jsondata
from ddt import ddt, data, unpack
from pages.cal_page import CalElement
import pytest



class TestCal():
    """
    计算测试 相当于业务层
    """
    @pytest.mark.parametrize('a,b,expect', get_jsondata('caladd.json'))
    def test_add(self, a, b, expect):
        """
        expect:我们预期值
        res:实际计算结果
        """
        print(a, b, expect)
        res = CalElement().add(a,b)   # 进行计算
        print(res)
        assert res == str(expect)

    # def test_devide(self):
    #     """测试减法"""
    #     pass
    #
    # def test_multiply(self):
    #     """测试乘法"""
    #     pass
    #
    # def test_devide(self):
    #     """测试除法"""
    #     pass

if __name__ == "__main__":
    testcal = TestCal()
    testcal.test_add()













