import logging
import datetime as dt

# logger实例化
logger = logging.getLogger('mylogger')

# 设置日志级别
logger.setLevel(logging.DEBUG)

# 将日志写到一个文件中，按大小按时切分
rf_handler = logging.handlers.TimedRotatingFileHandler(
    filename = '',when='midnight',interval=1,backupCount=7,atTime=dt.time(0,0,0,0)
)

# 对要写的日志进行格式定制
rf_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# 增加处理器进行处理
logger.addHandler(rf_handler)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
