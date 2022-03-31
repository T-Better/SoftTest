#test_parameters.py
import pytest

@pytest.mark.parametrize("x,y",[
    (3+5,8),
    (2+4,6),
    (6*9,42),
    ])
def test_add(x,y):
    assert x == y
