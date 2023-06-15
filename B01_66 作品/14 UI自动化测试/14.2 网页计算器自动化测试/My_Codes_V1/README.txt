需求：
    1、对网页计算器， 进行加法的测试操作。 通过读取数据文件中的数据来执行用例。
    2、网址： http://cal.apple886.com/
要求：
    1、使用PO模式的分层思想对页面进行封装
    2、使用参数化传入测试数据
    3、把测试数据定义到JSON数据文件中
    4、使用Pytest、Allure、Logging
    5、把基础数据从json换成xml、yaml等
   
测试点：
    1、加法：1+1=2 2+9！=10 ...
    2、减法：3-1=2 5-3！=8 ...
    3、乘法：2*3=6 5*7！=2 ...
    4、除法：8/2=4 9/3!=2 ...
版本：V1
技术：
    1、使用openpyxl读取excel每个sheet页数据，pytest.parametriez实现数据驱动（也可以读取json）
    2、使用pytest的fixture实现setup和teardown（打开浏览器访问网址并最大化，关闭浏览器）
    3、使用allure生成了测试报告
    4、使用loguru来生成测试日志文件
    5、使用了python的单例模式，自动化测试的PO思想
    6、使用了selenium对元素进行定位和控制