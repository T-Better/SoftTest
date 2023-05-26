import logging
import time as dt
import logging.handlers


fn = dt.strftime('{}'.format("%Y%m%d"))+".log"

logger = logging.getLogger('mylogger')

# 设置日志级别
logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler(
    filename='',when='midnight',interval=1,backupCount=7,atTime=dt.time(0,0,0,0)
)

rf_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))









