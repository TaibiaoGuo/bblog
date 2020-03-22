# !/usr/bin python3
# encoding:utf-8
'''
 @Time     :2020/3/23 4:17 AM
 @Author   :TaibiaoGuo
 @FileName :logUtils
 @Github   :https://github.com/TaibiaoGuo
 @Describe :
'''

import logging
from logging.handlers import RotatingFileHandler
from config import Config

logger = logging.getLogger('werkzeug')
logger.setLevel(logging.INFO)

# Inside the log folder in the current directory
LOG_PATH = Config.curr_dir + '/logs/'
# Project name
LOG_NAME = LOG_PATH + ""
# the object you will use
logger = logging

###
_str = "[%(asctime)s] [%(levelname)s] [%(filename)s<%(lineno)d>-%(module)s.%(funcName)s]: %(message)s"
formatter = logging.Formatter(_str)
logging.basicConfig(
    level=logging.DEBUG,
    format="---> [%(filename)s] %(funcName)s: %(message)s",
    # datefmt='%Y-%m-%d %H:%M:%S',
    # filename='crawler_info.log',
    # filemode='a'
)
# 定义RotatingFileHandler, 最多备份5个日志, 每个日志最大10M
config = {"mode": 'a', "maxBytes": 1024 * 1024 * 512, "backupCount": 5, "encoding": 'utf-8'}

# INFO
info_handler = RotatingFileHandler(LOG_NAME + 'info.log', **config)
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)
logging.getLogger('').addHandler(info_handler)

# DEBUG
debug_handler = RotatingFileHandler(LOG_NAME + 'debug.log', **config)
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(formatter)
logging.getLogger('').addHandler(debug_handler)

# ERROR
error_handler = RotatingFileHandler(LOG_NAME + 'error.log', **config)
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)
logging.getLogger('').addHandler(error_handler)

# linux 去除 requests 警告
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
