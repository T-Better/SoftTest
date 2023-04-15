import logging
import time

# 初始化Logger
logger = logging.getlogger('mylogger')

# 设置日志界别
logger.setLevel(logging.DEBUG)

# 将日志写入一个文件，按时按大小切分
rf_handler = logging.handlersTimeRomatatingFileHandler(
    filename = '',when='midnight',interval=1,backCount=7,atTime=dt.time(0,0,0,0)
)

# 定个时
rf_handler.setFormatter(logging.Formatter(''))


