import os


cpath = os.path.abspath(os.path.dirname(__file__))  # 当前路径 基础

# 改我们三儿就行
test_name = r'ASFF切换流程'  # 文件夹名字
bpmn_name = r'PP1.bpmn'  # bpmn文件名称
excel_name = r'PP2.xlsx'  # xlsx文件的名称

bpmn_path = r'{}\data\{}\{}'.format(cpath, test_name, bpmn_name)
excel_path = r'{}\data\{}\{}'.format(cpath, test_name, excel_name)

# mysql用
# 新的asff
asffhost = ''  # TODO 待填
asffport = '' # TODO 待填
asffpassword = ''  # TODO 待填
asffdbname = ''  # 用户名
asfftable = ''

# 旧的asff
# asffhost = ''  # TODO 待填
# asffport = '' # TODO 待填
# asffpassword = ''  # TODO 待填
# asffdbname = ''  # 用户名
# asfftable = ''