from loguru import logger
from config import BASE_DIR
import time

now_dt = time.strftime("%Y%m%d")
logpath = BASE_DIR + r'\log'
# logname = r'\\' + now_dt + r'.log'
cal_log = r'{}\\{}.log'.format(logpath,now_dt)
print(cal_log)
trace = logger.add(cal_log, rotation="5MB",encoding='utf-8',enqueue=True,retention="1 days")


