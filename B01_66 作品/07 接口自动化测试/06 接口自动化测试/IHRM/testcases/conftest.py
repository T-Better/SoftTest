import pytest
from api.login import IhrmLogin

@pytest.fixture(scope='session', autouse=True)
def login_fix():
    print('1')
      # login api实例化
    print('2')





