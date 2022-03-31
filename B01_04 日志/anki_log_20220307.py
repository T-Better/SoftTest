import logging

fmt = "%(filename)s %(funcName)s %(lineno)d"
logging.basicConfig(level=logging.WARNING, format = fmt)
logging.debug('调试')
logging.info('信息')
logging.warning('警告')
logging.error('错误')




