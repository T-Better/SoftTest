import pytest


@pytest.mark.skipif('指令')
def test_20220210():
    assert 1 == 2

@pytest.mark.skip('reason')
def test_unique_id_1():
    assert 1 == 3


