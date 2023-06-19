import pytest
from config import *

testfile = BASE_DIR + r'\testcases\test_cal_page.py'
pytest.main(['-s',testfile])
# print('over')