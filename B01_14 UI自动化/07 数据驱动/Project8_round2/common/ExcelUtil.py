from openpyxl import load_workbook
import os
"""封装读取数据文件的方法"""

class ExcelUtil(object):
    # 初始化，增加默认属性excel_path和sheet_name（默认值均为None）
    # 注意，代码中都不使用常量路径，而都使用变量路径，防止换个文件夹就跑不起来
    def __init__(self,# TODO):
        """获取excel工作表"""
        pass
        # TODO 9行

        # 打开工作表 2行
        # TODO

    def get_data(self):
        """
        获取文件数据
        每一行数据一个list case，所有的数据一个大list case_all:[['用例编号', '标题', '邮箱地址', '密码', '预期结果定位', '预期结果'], ['login-001', '登录成功', 'admin@tynam.com', 'tynam123', 'login success', '登录成功！'], ...
        注意要判断是否没内容，没内容的话就打印总行数小于1，没有数据  13行
        """
        # TODO



if __name__ == "__main__":
    # 调用并打印出数据 3行
    pass







