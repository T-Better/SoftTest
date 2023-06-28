# cal_testlog.py
import loguru
import time, os
from loguru import logger

BASE_DIR = os.path.abspath(os.path.dirname("__file__"))
now_dt = time.strftime("%Y%m%d")
logpath = BASE_DIR + r'\log'
cal_log = r'{}\\{}.log'.format(logpath,now_dt)
print(cal_log)
# 存于/log/20230606.log中
# 每10M为一个文件，满了就再分出来一个
# 里面的中文正确显示，无乱码
# 保存时间为10天，10天后清理10天前的
# 其他模块（test_a_log.py）执行过程也要记录进去








