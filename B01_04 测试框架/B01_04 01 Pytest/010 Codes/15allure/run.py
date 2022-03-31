import pytest
import os

if __name__ == "__main__":
    pytest.main(['-s', '../15allure/', '--alluredir', './result', '--clean-alluredir'])
    os.system('allure generate ./result -o ./report/report_all --clean')
    os.system('allure open -h 127.0.0.1 -p 8083 report/report_all/index.html')