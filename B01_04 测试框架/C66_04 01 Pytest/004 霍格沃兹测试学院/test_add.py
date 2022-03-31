def add(x,y):
    return x + y

def test_add():
    assert add(1, 10) == 11
    assert add(1, 1) == 2
    assert add(1, 99) == 100
class TestClass:
    def test_one(self):
        x = "this"
        print("测试-s")  # 未打印
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
        