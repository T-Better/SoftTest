# anki_日志复习_20220209.py
import logging

logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()

logging.basicConfig(level=logging.info)
"""
输出info及以上的日志到终端，包括文本形式的日志级别、日志输出函数的模块文件名、
日志输出函数的语句所在代码行、字符串形式的当前时间，如2022-02-01 时:分:秒;
用户输出的消息
"""
fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
logging.basicConfig(level=logging.INFO,format=fmt)


