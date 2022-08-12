import allure

# allure中缺陷标记等级有哪几种？各有啥含义
allure.blocker()
allure.critical()
allure.normal()
allure.minor()
allure.trivial()

# allure：命令行参数方式(pytest -v...)只运行test_severity.py中缺陷等级为blocker、critical的测试用例，并生成测试报告到allure文件夹中
# pytest test_severity.py -sq --alluredir=./allure --allure-severities=blocker,critical

# 类似@pytest.mark.xxx给不同的用例添加标记，如何用命令行方式（类似pytest -v）只运行epic名为test的测试用例
# pytest --alluredir ./report/allure --allure-epics=test


