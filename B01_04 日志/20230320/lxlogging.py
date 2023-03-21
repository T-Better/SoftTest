import logging
from logging import handlers
import datetime as dt

# logger实例化
logger = logging.Logger('mylogger')

# 设置日志记录级别
logger.setLevel(logging.DEBUG)

# 设置写到哪里
rf_handler = logging.handlers.TimedRotatingFileHandler(
    filename='20230320.log',when='midnight',interval=1,backupCount=7,atTime=dt.time(0,0,0,0)
)

# 写的格式
rf_handler.setFormatter(logging.Formatter('%(asctime)s-%(levelname)s-%(message)s'))


# 根据上面的配置 配置处理器
logger.addHandler(rf_handler)


logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

