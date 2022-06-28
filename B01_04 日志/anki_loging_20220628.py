import logging
from logging import handlers
import datetime

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
rf_handler = logging.handlers.TimeRotatingFileHandler(
    'all.log',when='midnight',backupCount=7,atTime=datetime.time(0,0,0,0)
)
rf_handler.setFormatter(logging.Formatter(''))
logger.addHandler(rf_handler)



