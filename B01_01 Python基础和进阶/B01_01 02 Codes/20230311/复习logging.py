import logging
"""
# 初始化logger
logger = logging.getLogger('mylogging')

# 设置Logger级别
logger.setLevel(logging.DEBUG)

rf_handler = logging.handlersTimedRotatingFileHandler(
    filename='',when = 'midnight',interval = 1,backupCount=7,atTime=dt.time(0,0,0,0)
)

rf_handler.setFomatter(logging.Formatter('%(asctime)s - %(levelname)s-%(message)s'))


logger.addHandler(rf_handler)



logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
"""

fmt = '%(filename)s %(funcName)s %(lineno)d'
logging.basicConfig(filename='a.log',level=logging.WARNING,format=fmt)



logging.debug('调试')
logging.info('信息')
logging.warning('警告')
logging.error('错误')