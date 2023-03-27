"""
要求将所有级别的所有日志都写入磁盘文件中
all.log文件中记录所有的日志信息，日志格式为：日期和时间 - 日志级别 - 日志信息
要求all.log在每天凌晨进行日志切割
"""
import logging
import logging.handlers
import datetime as dt


# 1、logger实例初始化
mylogger = logging.getLogger('logger')

# 2、设置日志处理级别
mylogger.setLevel(logging.DEBUG)

# 3、配置写到哪里，什么时候写等
rf_handler = logging.handlers.TimedRotatingFileHandler(
    filename ='20230301.log',when='midnight',interval = 1,backupCount=7,atTime=dt.time(0, 0, 0, 0)
)

# 4、配置日志书写格式
rf_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# 5、增加处理器进行处理
mylogger.addHandler(rf_handler)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')



