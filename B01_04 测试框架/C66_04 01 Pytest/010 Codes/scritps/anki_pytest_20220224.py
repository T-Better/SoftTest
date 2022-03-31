import pytest

@pytest.mark.run(order=1)
def test_step1():
    print("1")
    assert 1 == 1

@pytest.mark.run(order=2)
def test_step2():
    print("2")
    assert 2 == 1

