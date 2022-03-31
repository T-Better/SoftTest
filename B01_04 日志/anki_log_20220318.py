"""
• 要求将所有级别的所有日志都写入磁盘文件中
• all.log文件中记录所有的日志信息，日志格式为：日期和时间 - 日志级别 - 日志信息
• 要求all.log在每天凌晨进行日志切割
"""
import logging
import logging.handlers
import datetime

# 创建logger入口（造图纸）
logger = logging.getLogger('mylogger')
# 设置logger最低处理等级：DEBUG(设计最低标准)
logger.setLevel(logging.DEBUG)
# 制造手臂(配置handler)
rf_handler = logging.handlers.TimedRotatingFileHandler(
'all.log', when='midnight', interval=1, backupCount=7,atTime=datetime.time(0, 0, 0, 0))

# 为设计出的手臂处理器配置处理结果样式
rf_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)

# 最后：将手臂安装在机器人身上（为该handler设置写日志格式）
logger.addHandler(rf_handler)
