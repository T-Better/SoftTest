import logging
import logging.handlers
import datetime


logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
rf_handler = logging.handlers.TimedRotatingFileHandler(
    'all.log',when='midnight',backupCount=7,atTime=datetime.time(0,0,0,0)
)
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(mesage)s"))

logger.addHandler(rf_handler)
