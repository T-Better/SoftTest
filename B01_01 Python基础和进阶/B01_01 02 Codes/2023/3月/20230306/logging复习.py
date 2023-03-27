import logging


#
logger = logging.addLogger('mylogger')

#
logger.setLevel(logging.DEBUG)

#
rf_handler = logging.handlers.TimedRotatingFileHandler(
    filename='20230306.log',when='midnight',interval=1,backupCount=7,atTime=dt.time(0,0,0,0)
)

rf_handler.setFomatter(logging.Formatter(%(asctime)s - %(filename)s - %(message)s))

logger.addHandler(rf_handler)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')



