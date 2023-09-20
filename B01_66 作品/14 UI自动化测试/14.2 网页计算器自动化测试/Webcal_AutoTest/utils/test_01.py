"""
1.学习目标
    掌握带参数化fixture编写
2.操作步骤
    @pytest.fixture(params=[列表格式数据])
    request是pytest中内置关键字
3.需求
4.总结
    1.pytest fixture 主要是用来完成测试用例执行前后操作
        例如:测试前后对数据库连接/断开;打开/关闭浏览器APP
    2.fixture还可以用来准备测试数据
        带参数fixture
        有返回值fixture  (在实际工作中返回数据比较灵活，推荐使用)
    3.fixture中的参数
        scope: 确定fixture作用范围 默认function,class,module,session
        autouse:当值true时,相当于setup
        name: 对fixture重命名
"""
import pytest


# 编写fixture,带参数
@pytest.fixture(params=[("孙悟空", 666), ("猪八戒", 777), ("沙和尚", 888)])
def need_data(request):
    return request.param


def test_data(need_data):
    print(f"测试人物:{need_data[0]}")
    print(f"测试分数:{need_data[1]}")


if __name__ == '__main__':
    pytest.main()

"""
执行结果：
测试人物:孙悟空
测试分数:666
PASSED测试人物:猪八戒
测试分数:777
PASSED测试人物:沙和尚
测试分数:888
PASSED
"""