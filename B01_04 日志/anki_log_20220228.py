import logging

fmt = "%(filename)s - %(funcName)s - %(lineno)d"
logging.basicConfig(level=logging.INFO, format=fmt, filename='20220228.log')

logging.debug('调试')
logging.info('信息')
logging.warning('警告')
logging.error('错误')

logger.addHandler()
