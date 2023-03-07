import logging
import datetime as dt
import logging.handlers

# 创建记录器对象,括号中的pamslogger是记录器对象名称
logger = logging.getLogger('pamslogger')

# 配置日志记录级别
logger.setLevel(logging.DEBUG)

# 写到哪 何时配置
rf_handler = logging.handlers.TimedRotatingFileHandler(
    '20230303.txt',when='midnight',intervel=1,backupCount=7,atTime = dt.time(0,0,0,0)
)

# 如何写
rf_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(filename)s - %(levelname)s - %(message)s'
))

# 最后增加处理器
logger.addHandler(rf_handler)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
