import logging
import logging.handlers
import datetime as dt

# 初始化、实例化logger
mylogger = logging.getLogger('mylogger')

# 设置日志采集级别
mylogger.setLevel(logging.DEBUG)

# 日志写到哪里，什么时候写...
my_handler = logging.handlers.TimedRotatingFileHandler(
    '202302281951.log',when='midnight',interval = 1, backupCount=7,atTime=dt.time(0, 0, 0, 1)
)

mf_handler = my_handler.setFormatter(
    logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
)

mylogger.addHandler(mf_handler)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')



