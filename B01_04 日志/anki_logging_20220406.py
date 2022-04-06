"""
设置日志格式，要求：
1.自定义日志格式：调用日志输出函数的模块的文件名；
2.设置日志级别为warning;
3.自定义日志格式：调用日志输出函数的函数名；
4.调用日志输出函数的语句所在的代码行；
"""
import logging

fmt = "%(filename)s %(funcName)s %(lineno)d"
logging.basicConfig(level=logging.INFO, format=fmt)


logging.debug('调试')
logging.info('信息')
logging.warning('警告')
logging.error('错误')

# f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s"))



