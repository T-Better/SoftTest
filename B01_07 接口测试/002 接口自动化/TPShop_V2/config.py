import os


# 获取文件的绝对路径
abs_path = os.path.abspath(__file__)
print(abs_path)

# 日志路径 os.sep就是系统默认分隔符，windows是\
_log_path = abs_path + os.sep + 'log'

# 报告路径
_report_path = abs_path + os.sep + 'reports'

# 数据库信息配置
DB_CONFIG = {
    "host":"localhost",
    "user":"root",
    "password":"123456",
    "port":3306,
    "database":"tpshop2.0"
}

# 返回日志目录
def get_log_path():
    return _log_path

# 返回报告目录
def get_report_path():
    return _report_path

# 测试代码
if __name__ == "__main__":
    print(get_log_path())
    print(get_report_path())





