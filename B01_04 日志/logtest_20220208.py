# logtest_20220208.py
import logging

logging.debug('这是一条调试信息')
logging.info('这是一条普通信息')
logging.warning('这是一条警告信息')
logging.error('这是一条错误信息')
logging.critical('这是一条验证错误信息')
logging.basicConfig(level=logging.DEBUG)