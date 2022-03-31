# try_except_20220118.py
try:
    assert 1 == 2
except(NameError,ValueError) as res:
    raise error

