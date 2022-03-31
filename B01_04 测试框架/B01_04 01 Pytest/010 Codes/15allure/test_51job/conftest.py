import pytest

@pytest.fixture(scope="module")  # 每次调用该模块都会调用这个fixture
def open_51(login):
    name, token = login
    print(f"###用户 {name} 打开51job网站###")










