import logging
import logging.handlers
import time
import datetime as dt

fn = time.strftime('{}'.format('%Y%m%d'))+'.log' # 例如20230228.log
print(fn)

# 初始化logger
logger = logging.getLogger('mylogger')

# 设置日志级别
logger.setLevel(logging.DEBUG)

# 将日志写入一个文件，按时按大小切分
"""
Handler for logging to a file, rotating the log file at certain timed intervals.

If backupCount is > 0, when rollover is done, no more than backupCount
files are kept - the oldest ones are deleted.
"""
rf_handler = logging.handlers.TimedRotatingFileHandler(
filename = fn,when='midnight',interval=1,backupCount=7,atTime=dt.time(0,0,0,0)
)

# 对要写的日志内容定制格式,如
rf_handler.setFormatter(logging.Formatter('%(asctime)s-%(levelname)s-%(message)s'))

# 5、增加处理器进行处理
logger.addHandler(rf_handler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')





