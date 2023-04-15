import logging
import logging.handlers
import datetime

# 创建logger对象，是日志处理器handler的入口，将日志信息输出到指定输出中
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)  # 设置该logger对象的最低处理级别为DEBUG

# 将日志消息发送到磁盘文件，并支持日志文件按时间切割
# backupCount:日志文件备份数量。如果backupCount大于0，那么当生成新的日志文件时，将只保留backupCount个文件，删除最老的文件。
rf_handler = logging.handlers.TimedRotatingFileHandler(
    'all.log', when = 'midnight', interval=1, backupCount = 7,
)

atTime=datetime.time(0,0,0,0)  # ？这个是干啥的？
# 设置该logger的handler的输出格式
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - "
                        "%(filename)s[:%(lineno)d] - %(message)s"))
# 再新建一个handler处理器，用来写error.log，因为一般不是很多，所以不切片
# 将日志消息发送到磁盘文件，默认情况下文件大小会无限增长
f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)  # 为该handler设置最低等级
f_handler.setFormatter(
logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s")
)  # 为该handler设置写日志格式

logger.addHandler(rf_handler)  # 为该Logger对象添加一个handler
logger.addHandler(f_handler)  # 为该Logger对象添加一个handler

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')




