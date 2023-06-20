from loguru import logger
import time
from config import *


now_dt = time.strftime("%Y%m%d")
logpath = BASE_DIR + r'\log'
ihrm_log = r'{}\\{}.log'.format(logpath,now_dt)
trace = logger.add(ihrm_log, rotation='10MB',encoding="utf-8", enqueue = True, retention="1 days")





