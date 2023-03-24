# anki_pytest_20220130.py
import pytest

@pytest.fixture
def a():
    # 准备
    yield
    # 收尾
    return 1

