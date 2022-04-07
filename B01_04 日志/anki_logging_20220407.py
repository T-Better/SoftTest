import logging

fmt = "%(asctime)s %(levelname)s - %(msg)s"
logging.basicConfig(level=logging.INFO,format = fmt)

logging.debug('调试')
logging.info('信息')
logging.warning('警告')
logging.error('错误')

