import logging

fmt = '%(asctime)s %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format = fmt)


fmt2 = '%(filename)s %(funcName)s - %(lineno)d'
logging.basicConfig(level=logging.WARINIG,format=fmt2)


logging.debug('调试')
logging.info('信息')
logging.warning('警告')
logging.error('错误')


