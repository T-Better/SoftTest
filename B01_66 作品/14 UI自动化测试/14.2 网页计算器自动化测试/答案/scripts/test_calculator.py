import json
import pytest
from ..utils import DriverUtil
from ..page.calculator_page import CalculatorProxy

def build_data():
    test_data = []
    with open("../data/calculator.json", encoding='UTF-8') as f:
        test_data = json.load(f)
    print("test_data=",test_data)
    return test_data

class TestCalculator():
    def setup_class(self):
        self.driver  = DriverUtil.get_driver()
        self.calculatorProxy = CalculatorProxy()

    def teardown_class(self):
        DriverUtil.quit_driver()

    @pytest.mark.parametrize("a,b,expect", build_data())
    def test_add(self, a,b, expect):
        print('a={} b={} expect={}'.format(a, b, expect))
        self.calculatorProxy.add(a,b)
        # 获取计算结果
        result = self.calculatorProxy.get_result()
        print("result=",result)
        assert result == str(expect)