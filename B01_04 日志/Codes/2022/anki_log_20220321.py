import logging
import logging.handlers
import datetime

# 第一步，造图纸
logger = logging.getLogger('mylogger')

# 第二步：说明产品制造的最低标准
logger.setLevel(logging.DEBUG)

# 第三步：制造手臂：配置handler
rf_handler = logging.handlers.TimedRotatingFileHandler(
    'all.log',when='midnight',interval=1, backupCount=7, atTime=datetime.time(0,0,0,0))

# 第四步：为设计出的手臂处理器配置书写结果样式
rf_handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
))

# 第五步：将手臂安装在机器人身上
logger.addHandler(rf_handler)


