import logging
import logging.handlers
import datetime

logger = logging.getLogger('mylogger')

logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler('all.log',when='midnight',1,backupCount=7,atTime=datetime.time(0,0,0,0))

rf_handler.setFormatter(logging.Formatter())

logger.addHandler(rf_handler)

