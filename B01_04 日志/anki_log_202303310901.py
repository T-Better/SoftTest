import logging
from logging import handlers
import datetime as dt

# 创建logger实例对象
logger = logging.getLogger('mylogger')

# 配置logger采日志界别
logger.setLevel(logging.DEBUG)

# 开始配置日志分割等
rf_handler = logging.handlers.TimedRotatingFileHandler(
    filename='20230331.log', when='midnight',interval=1,backupCount=7,atTime=dt.time(0,0,0,0)
)

# 配置handler的日志书写格式
rf_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# 把配置好的handler装上
logger.addHandler(rf_handler)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

