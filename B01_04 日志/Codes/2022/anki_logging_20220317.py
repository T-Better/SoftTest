"""
1）要求将所有级别的所有日志都写入磁盘文件中:DEBUG
2）all.log文件中记录所有的日志信息，日志格式为：日期和时间 - 日志级别 - 日志信息
3）error.log文件中单独记录error及以上级别的日志信息，日志格式为：日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
4）要求all.log在每天凌晨进行日志切割:logging.handlers.TimedRotatingFileHandler、FileHandler
"""

import logging
import datetime
import logging.handlers

# 创建all.log的logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# 将日志消息发送到磁盘文件，并支持日志文件按时间切割
rf_handler = logging.handlers.TimeRotatingFileHandler(
    'all.log', when='midnight', interval=1, backupCount=7,atTime=datetime.time(0,0,0,0)
)
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# 创建error.log的Logger
f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter(
"%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"
))

logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')

logger.setLevel(logging.DEBUG)