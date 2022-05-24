import logging

logging.basicConfig(filename='a.log')

formatter = logging.Formatter(fmt=None,datefmt=None,style='%')
logger = logging.getlogger('mulogger')

logger.serlevel(logging.DEBUG)

formatter1 = handler.setFormatter()
